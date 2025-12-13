from __future__ import annotations
from abc import ABC, abstractmethod


class Juice(ABC):
    """
    Abstract class that defines the template method (algorithm skeleton)
    for making juice, while allowing subclasses to customize certain steps.
    """

    # Template Method (fixed sequence)
    def makeJuiceFromMe(self) -> None:
        self.peelFruit()
        self.addToGrinder()
        self.addCondiments()
        self.grind()
        self.pour()

    # Steps that vary (must be implemented differently)
    @abstractmethod
    def peelFruit(self) -> None:
        pass

    @abstractmethod
    def addToGrinder(self) -> None:
        pass

    # Common/default steps (shared)
    def addCondiments(self) -> None:
        print("addCondiments: adding milk and sugar")

    def grind(self) -> None:
        print("grind: grinding the mixture")

    def pour(self) -> None:
        print("pour: pouring into a cup")
