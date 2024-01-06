from ..element import BlockElement, InlineElement, ElementList, Text
from ..inline.emphasis import Bold, Italic, BoldItalic


class Link(BlockElement):
    def __init__(self, url: str, text: str | Bold | Italic | BoldItalic = "",  title: str = "") -> None:
        super().__init__()
        self.url = url
        self.text = Text(text) if isinstance(text, str) else text
        self.title = title

    def md_str(self) -> str:
        if self.text == "":
            return f"<{self.url}>"
        else:
            return f"[{self.text.md_str()}]({self.url}{f" \"{self.title}\"" if self.title!="" else ""})"

    def __repr__(self) -> str:
        return super().__repr__(text=self.text, url=self.url, title=self.title)