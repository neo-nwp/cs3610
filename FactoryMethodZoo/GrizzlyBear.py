from FactoryMethodZoo.IAnimal import IAnimal
class GrizzlyBear(IAnimal):
    def say(self) -> str: return "GrizzlyBear: Roar"
