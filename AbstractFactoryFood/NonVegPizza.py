from AbstractFactoryFood.Pizza import Pizza

class NonVegPizza(Pizza):
    def get_Description(self) -> str:
        return f"{self._desc} (Size: {self._size})"

    def showNonVegPizzaAdver(self) -> str:
        return f"Non-Veg Pizza Ad: {self.get_Description()} - ${self.get_Price()}"