from AbstractFactoryFood.Burger import Burger

class NonVegBurger(Burger):
    def get_Description(self) -> str:
        return self._desc

    def showNonVegBurgerAdver(self) -> str:
        return f"Non-Veg Burger Ad: {self.get_Description()} - ${self.get_Price()}"