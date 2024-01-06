from abc import ABCMeta, abstractmethod
from typing import Self

from ..element import BlockElement, Text, ElementList, MdElement
from .blockquote import Blockquote
from .image import Image
from .paragraph import Paragraph


class List(BlockElement, metaclass=ABCMeta):
    def __init__(self, *items: tuple[str | Paragraph | Blockquote | Image | Self]) -> None:
        super().__init__()

        self.items = [Text(item) if isinstance(item, str)
                      else ElementList(tuple(item)) for item in items]

    @abstractmethod
    def md_str(self) -> str:
        ...

    def __repr__(self) -> str:
        return super().__repr__(items=self.items)


class OrderedList(List):
    def md_str(self) -> str:
        md = ""
        for ind, item in self.items:
            md += f"{ind}. {item}\n"


class UnorderedList(List):
    ...
