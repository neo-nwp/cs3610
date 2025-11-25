from AbstractFactoryFood.Noodles import Noodles

class NonVegNoodles(Noodles):
    def get_Description(self) -> str:
        return self._desc

    def showNonVegNoodlesAdver(self) -> str:
        return f"Non-Veg Noodles Ad: {self.get_Description()} - ${self.get_Price()}"