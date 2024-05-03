from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import coiled
from pytask import DataCatalog
from pytask_parallel import ParallelBackend
from pytask_parallel import registry

if TYPE_CHECKING:
    from concurrent.futures import Executor

SRC = Path(__file__).parent
BLD = SRC.parent.parent / "bld"


def _build_client(n_workers: int) -> Executor:
    return (
        coiled.Cluster(n_workers=n_workers, name="coiled-project")
        .get_client()
        .get_executor()
    )


registry.register_parallel_backend(ParallelBackend.CUSTOM, _build_client, remote=True)


data_catalog = DataCatalog()
