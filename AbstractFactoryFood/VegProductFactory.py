from AbstractFactoryFood.IProductFactory import IProductFactory
from AbstractFactoryFood.VegBurger import VegBurger
from AbstractFactoryFood.VegPizza import VegPizza
from AbstractFactoryFood.VegNoodles import VegNoodles

class VegProductFactory(IProductFactory):
    def createBurger(self, price: int, calories: int, desc: str) -> VegBurger:
        return VegBurger(price, calories, desc)
    def createPizza(self, price: int, calories: int, desc: str, size: str) -> VegPizza:
        return VegPizza(price, calories, desc, size)
    def createNoodles(self, price: int, calories: int, desc: str) -> VegNoodles:
        return VegNoodles(price, calories, desc)