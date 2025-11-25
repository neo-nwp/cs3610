from FactoryMethodZoo.IAnimal import IAnimal
class Lion(IAnimal):
    def say(self) -> str: return "Lion : Roaring"
