from FactoryMethodZoo.IAnimal import IAnimal
class Moose(IAnimal):
    def say(self) -> str: return "Moose : Bellow"
