from ..element import BlockElement, InlineElement, ElementList


class HorizontalRule(BlockElement):
    def __init__(self) -> None:
        super().__init__()

    def md_str(self) -> str:
        return "---"
