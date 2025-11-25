from FactoryMethodZoo.IAnimal import IAnimal
class Penguin(IAnimal):
    def say(self) -> str: return "Penguin : Honk"
