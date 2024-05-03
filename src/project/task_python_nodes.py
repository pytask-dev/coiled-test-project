from pytask import Product
from pytask import PythonNode
from typing_extensions import Annotated

from project.config import BLD

first_part = PythonNode()


def task_first(node: Annotated[PythonNode, first_part, Product]) -> None:
    node.save("Hello ")


full_text = PythonNode()


def task_second(first_part: Annotated[str, first_part]) -> Annotated[str, full_text]:
    return first_part + "World!"


def task_third(
    full_text: Annotated[str, full_text],
) -> Annotated[str, BLD / "python_nodes" / "output.txt"]:
    assert full_text == "Hello World!"
    return full_text
