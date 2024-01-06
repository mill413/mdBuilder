from enum import Enum, auto

from ..block.link import Link
from ..element import BlockElement, ElementList, Text
from ..inline.code import Code
from ..inline.emphasis import Bold, BoldItalic, Italic

TableElements = list[str, Link, Code, Bold, Italic, BoldItalic]


class Alignment(Enum):
    LEFT = ":---"
    RIGHT = "---:"
    CENTER = ":---:"


class Table(BlockElement):
    def __init__(self,
                 header: TableElements,
                 content: list[TableElements],
                 alignment: list[Alignment] = []) -> None:
        super().__init__()
        self.headers = ElementList(tuple(header))
        self.contents = [ElementList(row) for row in content]
        self.alignments = alignment
        
        self.fill_none_items()

    def md_str(self) -> str:
        header_md = f"| {" | ".join(
            self.replace_pipes(self.headers.md_str_list())
        )} |"
        content_md = "\n".join([
            f"| {" | ".join(self.replace_pipes(row.md_str_list()))} |"
            for row in self.contents])
        alignment_md = f"| {
            " | ".join([alignment.value for alignment in self.alignments])} |"
        return "\n".join((header_md, alignment_md, content_md))

    def fill_none_items(self):
        max_columns = max((
            len(self.headers),
            *(len(content) for content in self.contents),
            len(self.alignments)
        ))

        if len(self.headers) < max_columns:
            self.headers.extend(" "*(max_columns - len(self.headers)))
        for row in self.contents:
            if len(row) < max_columns:
                row.extend(" "*(max_columns - len(row)))
        if len(self.alignments) < max_columns:
            self.alignments.extend(
                Alignment.LEFT*(max_columns - len(self.alignments)))

    def replace_pipes(self, str_list: list[str]) -> list[str]:
        return [str.replace("|", "&#124;") for str in str_list]
