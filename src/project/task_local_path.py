from pathlib import Path

from pytask import Product
from typing_extensions import Annotated

from project.config import BLD


def task_create_local_path_node(
    path: Annotated[Path, Product] = BLD / "local_path" / "first.txt",
) -> None:
    path.write_text("Hello,")


def task_use_local_path_return(
    path: Annotated[Path, BLD / "local_path" / "first.txt"],
) -> Annotated[str, BLD / "local_path" / "second.txt"]:
    return path.read_text() + " World!"


def task_local_file_check(path: Path = BLD / "local_path" / "second.txt") -> None:
    assert path.read_text() == "Hello, World!"
