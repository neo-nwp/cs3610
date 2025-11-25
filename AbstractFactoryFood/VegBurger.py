from AbstractFactoryFood.Burger import Burger

class VegBurger(Burger):
    def get_Description(self) -> str:
        return self._desc

    def showVegBurgerAdver(self) -> str:
        return f"Veg Burger Ad: {self.get_Description()} - ${self.get_Price()}"