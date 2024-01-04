from abc import ABCMeta, abstractmethod
from typing import Self


class MdElement(metaclass=ABCMeta):

    @abstractmethod
    def md_str(self) -> str:
        pass

    def __repr__(self, show_more=False, **info: dict) -> str:
        base_info = {
            "name": self.__class__.__name__,
            "markdown": self.md_str()
        }
        return str(base_info.update(info) if show_more else base_info)


class InlineElement(MdElement, metaclass=ABCMeta):
    def __init__(self, content: str, symbol: str) -> None:
        super().__init__()
        self.content = content
        self.symbol = symbol

    def md_str(self) -> str:
        return f"{self.symbol}{self.content}{self.symbol}"


class BlockElement(MdElement, metaclass=ABCMeta):
    def __init__(self, *content: tuple[MdElement, str]) -> None:
        super().__init__()
        self.content = [Text(str) if isinstance(
            element, str) else element for element in content]

    def md_str(self) -> str:
        return "\n".join(self.content)


class Text(MdElement):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.content = text

    def md_str(self) -> str:
        return self.content


class ElementList:
    def __init__(self, elements: tuple[MdElement, str, Self]) -> None:
        self.elements: list[MdElement] = [
            Text(e) if isinstance(e, str) else e for e in elements]

    def md_str_list(self) -> list[str]:
        return [e.md_str() for e in self.elements]

    def __repr__(self) -> str:
        return self.__class__.__name__+str([e.__repr__() for e in self.elements])
