from AbstractFactoryFood.Noodles import Noodles

class VegNoodles(Noodles):
    def get_Description(self) -> str:
        return self._desc

    def showVegNoodlesAdver(self) -> str:
        return f"Veg Noodles Ad: {self.get_Description()} - ${self.get_Price()}"