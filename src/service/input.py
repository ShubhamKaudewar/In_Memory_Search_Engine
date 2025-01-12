from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple, List, Any


class InputController:
    def input(self, action: str) -> Any:
        if action.upper() == "INSERT":
            return InputInsert().take_input()
        elif action.upper() == "SEARCH":
            return InputSearch().take_input()
        else:
            raise ValueError(f"Invalid input action: {action}")

class Input(ABC):
    @abstractmethod
    def take_input(self) -> Any:
        pass


class InputInsert(Input):
    def take_input(self) -> List[str]:
        print("provide documents: e.g. 'I am Indian,I am developer'")
        documents = [x for x in input("provide documents: ").split(",")]
        # documents = ["I am Indian", "I am an developer", "Raj is an Indian Developer", "Bob is not developer"]
        return documents


class InputSearch(Input):
    def take_input(self) -> Tuple[List[str], str]:
        print("provide keywords: e.g. 'I,am'")
        keywords = [x for x in input("provide keywords: ").split(",")]
        # keywords = ["I", "am"]
        print("provide operation: [AND, OR, NOT]")
        operation = input("provide operation: ")
        # operation = "and"
        return keywords, operation