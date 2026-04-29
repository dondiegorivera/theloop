"""TaskAdapter registry."""

from __future__ import annotations

from theloop.adapters.base import RuntimeCheckResult, TaskAdapter
from theloop.adapters.doc import DocAdapter
from theloop.adapters.generic import GenericAdapter
from theloop.adapters.svg import SVGAdapter
from theloop.adapters.web import WebAppAdapter

ADAPTERS: dict[str, type[TaskAdapter]] = {
    "svg": SVGAdapter,
    "web": WebAppAdapter,
    "generic": GenericAdapter,
    "doc": DocAdapter,
}


def get_adapter(name: str) -> TaskAdapter:
    cls = ADAPTERS.get(name)
    if cls is None:
        raise ValueError(
            f"unknown adapter {name!r}; available: {sorted(ADAPTERS)}"
        )
    return cls()


__all__ = [
    "TaskAdapter",
    "RuntimeCheckResult",
    "SVGAdapter",
    "WebAppAdapter",
    "GenericAdapter",
    "DocAdapter",
    "get_adapter",
    "ADAPTERS",
]
