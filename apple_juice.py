from juice import Juice


class AppleJuice(Juice):
    def peelFruit(self) -> None:
        print("peelFruit: peeling the apple")

    def addToGrinder(self) -> None:
        print("addToGrinder: cutting apple into pieces, then adding to grinder")
