from mdElement import MdElement,InlineElement, BlockElement,Paragraph
from pathlib import Path


class MdWriter:
    def __init__(self,
                 *content: tuple[MdElement]) -> None:
        self.content: list[MdElement] = [Paragraph(c) if isinstance(c, InlineElement) else c for c in content]

    def write_to_file(self, file: str | Path, mode="w"):
        md_file = file if isinstance(file, Path) else Path(file)

        assert md_file.exists(), f"{file} doesn't exist!"

        content_str: str = "\n".join([block.md_str()+"\n"
                                     for block in self.content])

        with open(md_file, mode) as f:
            f.write(content_str)
