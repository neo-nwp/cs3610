from abc import ABC, abstractmethod
from AbstractFactoryFood.Burger  import Burger
from AbstractFactoryFood.Pizza   import Pizza
from AbstractFactoryFood.Noodles import Noodles

class IProductFactory(ABC):
    @abstractmethod
    def createBurger(self, price: int, calories: int, desc: str) -> Burger: ...
    @abstractmethod
    def createPizza(self, price: int, calories: int, desc: str, size: str) -> Pizza: ...
    @abstractmethod
    def createNoodles(self, price: int, calories: int, desc: str) -> Noodles: ...