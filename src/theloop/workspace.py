"""Per-run workspace + git plumbing.

Each run lives in `runs/<run_id>/`:

    runs/<run_id>/
    ├── workspace/         ← git repo; pi edits files here
    │   ├── .git/
    │   └── ...adapter-scaffolded files
    └── artifacts/
        ├── iter-0/        ← screenshots, judge verdicts, etc.
        └── iter-1/

Branch layout:
    main         ← initial scaffold commit
    iter/0       ← branched from main; one commit per iteration
    iter/1       ← branched from iter/0
    ...

Each iteration calls `begin_iteration(N)` (checks out the parent branch so pi
sees the right state) and then `commit_iteration(N, intent)` after pi
finishes. Failures are intentionally allowed to raise — the Loop decides
whether to keep going.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime
from pathlib import Path

import git

log = logging.getLogger(__name__)

_SLUG_RE = re.compile(r"[^a-z0-9]+")


def make_run_id(slug: str | None = None, *, now: datetime | None = None) -> str:
    """`YYYYMMDD-HHMMSS[-slug]`. Slug is lowercased, alnum + dashes, capped at 30."""
    ts = (now or datetime.now()).strftime("%Y%m%d-%H%M%S")
    if not slug:
        return ts
    clean = _SLUG_RE.sub("-", slug.lower()).strip("-")[:30]
    return f"{ts}-{clean}" if clean else ts


class Workspace:
    def __init__(self, run_dir: Path, repo: git.Repo) -> None:
        self.run_dir = run_dir
        self.repo = repo

    # ── construction ──────────────────────────────────────────────────────

    @classmethod
    def create(
        cls,
        runs_root: Path,
        run_id: str | None = None,
        slug: str | None = None,
    ) -> Workspace:
        run_id = run_id or make_run_id(slug)
        run_dir = runs_root / run_id
        ws_path = run_dir / "workspace"
        (run_dir / "artifacts").mkdir(parents=True, exist_ok=True)
        ws_path.mkdir(parents=True, exist_ok=True)

        repo = git.Repo.init(ws_path, initial_branch="main")
        with repo.config_writer() as cw:
            cw.set_value("user", "name", "theloop")
            cw.set_value("user", "email", "theloop@local")
            cw.set_value("commit", "gpgsign", "false")
        # initial empty commit so subsequent `checkout -b` has a HEAD
        repo.git.commit("--allow-empty", "-m", "scaffold")
        log.info("workspace created: %s (run_id=%s)", ws_path, run_id)
        return cls(run_dir, repo)

    @classmethod
    def open(cls, run_dir: Path) -> Workspace:
        repo = git.Repo(run_dir / "workspace")
        return cls(run_dir, repo)

    # ── paths ─────────────────────────────────────────────────────────────

    @property
    def workspace_path(self) -> Path:
        return Path(self.repo.working_dir)

    @property
    def artifacts_path(self) -> Path:
        return self.run_dir / "artifacts"

    def artifact_dir(self, iter_n: int) -> Path:
        d = self.artifacts_path / f"iter-{iter_n}"
        d.mkdir(parents=True, exist_ok=True)
        return d

    # ── iteration lifecycle ──────────────────────────────────────────────

    def begin_iteration(self, iter_n: int) -> None:
        """Check out the parent branch so the next iteration starts clean."""
        parent = "main" if iter_n == 0 else f"iter/{iter_n - 1}"
        self.repo.git.checkout(parent)
        log.debug("checked out %s for iter %d", parent, iter_n)

    def commit_iteration(self, iter_n: int, intent: str) -> str:
        """Create branch `iter/N`, stage everything in the workspace, commit.

        Returns the commit SHA. Always succeeds even if no files changed
        (uses --allow-empty), so each iteration has a stable ref.
        """
        branch = f"iter/{iter_n}"
        self.repo.git.checkout("-b", branch)
        self.repo.git.add("-A")
        first_line = (intent or "").strip().splitlines()[0:1]
        subject = first_line[0][:72] if first_line else ""
        msg = f"iter {iter_n}: {subject}" if subject else f"iter {iter_n}"
        self.repo.git.commit("-m", msg, "--allow-empty")
        sha = self.repo.head.commit.hexsha
        log.info("committed %s (%s) on %s", sha[:8], msg, branch)
        return sha

    def diff_iteration(self, iter_n: int) -> str:
        """Diff between this iter's parent and this iter."""
        base = "main" if iter_n == 0 else f"iter/{iter_n - 1}"
        return self.repo.git.diff(base, f"iter/{iter_n}")


# ── manual smoke test ───────────────────────────────────────────────────────

def _smoke() -> None:
    """Usage: python -m theloop.workspace"""
    import tempfile

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    with tempfile.TemporaryDirectory(prefix="theloop-ws-") as tmp:
        runs = Path(tmp)
        ws = Workspace.create(runs, slug="pelican-test")
        print(f"run_dir: {ws.run_dir.name}")
        print(f"branches initially: {[b.name for b in ws.repo.branches]}")

        # iter 0
        ws.begin_iteration(0)
        (ws.workspace_path / "artifact.svg").write_text("<svg>v0</svg>")
        sha0 = ws.commit_iteration(0, "first sketch of the pelican")
        ad0 = ws.artifact_dir(0)
        (ad0 / "screenshot.txt").write_text("fake png")

        # iter 1
        ws.begin_iteration(1)
        (ws.workspace_path / "artifact.svg").write_text("<svg>v1 with wings</svg>")
        sha1 = ws.commit_iteration(1, "add wings\nsecond line ignored")

        print(f"branches after 2 iters: {sorted(b.name for b in ws.repo.branches)}")
        print(f"iter/0 sha: {sha0[:8]}")
        print(f"iter/1 sha: {sha1[:8]}")
        diff = ws.diff_iteration(1)
        print(f"diff iter 0 → 1: {len(diff)} chars")
        assert "v0" in diff and "v1 with wings" in diff
        assert (ws.run_dir / "artifacts" / "iter-0" / "screenshot.txt").exists()
        print("✓ all assertions passed")


if __name__ == "__main__":
    _smoke()
