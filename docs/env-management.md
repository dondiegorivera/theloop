  - uv sync — installs/updates deps from pyproject.toml into .venv, writes/updates uv.lock. Run after editing pyproject.toml.    
  - uv add <pkg> / uv add --dev <pkg> — the friendlier way to add a dep; edits pyproject.toml + syncs in one go.               
  - uv run <cmd> — runs a command inside the venv without you needing to source .venv/bin/activate first. (That's how I just ran 
  the smoke test.)                                                                                                               
  - uv lock --upgrade-package <pkg> — bumps a single pinned dep when you want to.                                                
  - uv.lock is committed; .venv/ is not (already gitignored).  