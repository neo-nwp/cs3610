from abc import ABC, abstractmethod
from AbstractFactoryFood.IProduct import IProduct

class Noodles(IProduct, ABC):
    def __init__(self, price: int, calories: int, desc: str):
        self._price = price
        self._calories = calories
        self._desc = desc

    def get_Price(self) -> int:      return self._price
    def get_Calories(self) -> int:   return self._calories

    @abstractmethod
    def get_Description(self) -> str: ...