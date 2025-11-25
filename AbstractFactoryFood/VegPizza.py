from AbstractFactoryFood.Pizza import Pizza

class VegPizza(Pizza):
    def get_Description(self) -> str:
        return f"{self._desc} (Size: {self._size})"

    def showVegPizzaAdver(self) -> str:
        return f"Veg Pizza Ad: {self.get_Description()} - ${self.get_Price()}"