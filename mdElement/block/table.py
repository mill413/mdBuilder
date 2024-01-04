from mdElement.element import MdElement
from ..element import BlockElement

class Table(BlockElement):
    def __init__(self, header, alignment, content) -> None:
        super().__init__(*content)
        # TODO