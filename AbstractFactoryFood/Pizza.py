from abc import ABC, abstractmethod
from AbstractFactoryFood.IProduct import IProduct

class Pizza(IProduct, ABC):
    def __init__(self, price: int, calories: int, desc: str, size: str):
        self._price = price
        self._calories = calories
        self._desc = desc
        self._size = size

    # concrete universal behaviour
    def get_Price(self) -> int:      return self._price
    def get_Calories(self) -> int:   return self._calories
    def get_Size(self) -> str:       return self._size

    # leave description to subclasses
    @abstractmethod
    def get_Description(self) -> str: ...