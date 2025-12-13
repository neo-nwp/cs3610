from juice import Juice


class OrangeJuice(Juice):
    def peelFruit(self) -> None:
        print("peelFruit: peeling the orange")

    def addToGrinder(self) -> None:
        print("addToGrinder: dividing orange into slices, then adding to grinder")
