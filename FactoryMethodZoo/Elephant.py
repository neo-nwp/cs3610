from FactoryMethodZoo.IAnimal import IAnimal
class Elephant(IAnimal):
    def say(self) -> str: return "Elephant : Trumpet"
