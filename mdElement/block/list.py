from abc import ABCMeta, abstractmethod
from typing import Self

from ..element import BlockElement, Text, ElementList, MdElement
from .blockquote import Blockquote
from .image import Image
from .paragraph import Paragraph

ListItem = str | Paragraph | Blockquote | Image | Self


class List(BlockElement, metaclass=ABCMeta):
    def __init__(self, *items: tuple[str | list[ListItem]]) -> None:
        super().__init__()
        self.items: list[str|list[ListItem]] = list(items)
        print(self.items)
        self.check_str(self.items)

    @abstractmethod
    def md_str(self) -> str:
        ...

    def __repr__(self) -> str:
        return super().__repr__(items=self.items)

    def check_str(self, item_list: list) -> bool:
        for ind, item in enumerate(item_list):
            if ind == 0:
                assert isinstance(
                    item, str), "First element in a list item should be str"
            elif isinstance(item, list):
                self.check_str(item)


class OrderedList(List):
    def md_str(self) -> str:
       pass


class UnorderedList(List):
    def md_str(self) -> str:
        md_str_list = []
        for ind, item in enumerate(self.items):
            if isinstance(item, str):
                md_str_list.append(f"* {item}")
            else:
                sub_str_list = []
                for ind, e in enumerate(item):
                    if ind == 0 and isinstance(e, str):
                        md_str_list.append(f"* {e}")
                    else:
                        if isinstance(e, str):
                            sub_str_list.append(f"    {e}")
                        else:
                            sub_str_list.append(f"    {e.md_str()}")
                md_str_list.append(f"\n{"\n\n".join(sub_str_list)}\n")

        return "\n".join(md_str_list)