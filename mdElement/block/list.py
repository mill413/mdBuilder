from abc import ABCMeta, abstractmethod
from typing import Self, Sequence

from ..element import BlockElement, Text, ElementList, MdElement
from .blockquote import Blockquote
from .image import Image
from .paragraph import Paragraph

ListItem = Text | Paragraph | Blockquote | Image | Self


class List(BlockElement, metaclass=ABCMeta):
    def __init__(self, *items: tuple[str | list[str | Paragraph | Blockquote | Image | Self]]) -> None:
        super().__init__()
        self.items: list[list[ListItem]] = [
            [Text(item)] if isinstance(item, str)
            else [Text(i) if isinstance(i, str)
                  else i
                  for i in item]
            for item in items
        ]
        print(self.items)
        for item in self.items:
            self._check_list_(item)

    def md_str(self, nest_level: int = 0) -> str:
        return self._to_md_str_(nest_level)

    def __repr__(self) -> str:
        return super().__repr__(items=self.items)

    def _check_list_(self, item_list: list[ListItem]) -> bool:
        for ind, item in enumerate(item_list):
            if ind == 0:
                assert isinstance(
                    item, Text), "First element in a list item should be str"
            else:
                assert isinstance(
                    item, (Text, Paragraph, Blockquote, Image, List)), "The element must be paragraph, blockquote, image or list"

    @abstractmethod
    def _to_md_str_(self, nest_level: int = 0) -> str:
        ...


class OrderedList(List):
    def _to_md_str_(self, nest_level: int = 0) -> str:
        md_str_list = []
        indent = "    "*nest_level
        for item_ind, item_list in enumerate(self.items):
            if len(item_list) == 1:
                md_str_list.append(
                    f"{indent}{item_ind}. "+item_list[0].md_str())
            else:
                for ind, item in enumerate(item_list):
                    item_str_list = [
                        f"{indent}{item_ind}. "+item.md_str() if ind == 0
                        else
                        f"\n{indent}    "+item.md_str() if isinstance(item, (Text, Paragraph, Blockquote, Image))
                        else item.md_str(nest_level=nest_level+1)
                    ]
                    md_str_list.append("\n".join(item_str_list))

        return "\n".join(md_str_list)


class UnorderedList(List):
    def _to_md_str_(self, nest_level: int = 0) -> str:
        md_str_list = []
        indent = "  "*nest_level
        for _, item_list in enumerate(self.items):
            if len(item_list) == 1:
                md_str_list.append(f"{indent}* "+item_list[0].md_str())
            else:
                for ind, item in enumerate(item_list):
                    item_str_list = [
                        f"{indent}* "+item.md_str() if ind == 0
                        else
                        f"\n{indent}    "+item.md_str() if isinstance(item, (Text, Paragraph, Blockquote, Image))
                        else item.md_str(nest_level=nest_level+1)
                    ]
                    md_str_list.append("\n".join(item_str_list))

        return "\n".join(md_str_list)
