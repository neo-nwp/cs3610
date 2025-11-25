from AbstractFactoryFood.IProductFactory import IProductFactory
from AbstractFactoryFood.NonVegBurger import NonVegBurger
from AbstractFactoryFood.NonVegPizza import NonVegPizza
from AbstractFactoryFood.NonVegNoodles import NonVegNoodles

class NonVegProductFactory(IProductFactory):
    def createBurger(self, price: int, calories: int, desc: str) -> NonVegBurger:
        return NonVegBurger(price, calories, desc)
    def createPizza(self, price: int, calories: int, desc: str, size: str) -> NonVegPizza:
        return NonVegPizza(price, calories, desc, size)
    def createNoodles(self, price: int, calories: int, desc: str) -> NonVegNoodles:
        return NonVegNoodles(price, calories, desc)