from typing import cast

from pytask import PickleNode
from pytask import Product
from typing_extensions import Annotated

from project.config import BLD
from project.config import data_catalog


def task_create_data_catalog_node(
    node: Annotated[PickleNode, Product] = cast(PickleNode, data_catalog["first"]),  # noqa: B008
) -> None:
    node.save("Hello,")


def task_use_data_catalog_return(
    text: Annotated[str, data_catalog["first"]],
) -> Annotated[str, data_catalog["second"]]:
    return text + " World!"


def task_data_catalog_check(
    text: Annotated[str, data_catalog["second"]],
) -> Annotated[str, BLD / "data_catalog" / "output.txt"]:
    assert text == "Hello, World!"
    return text
