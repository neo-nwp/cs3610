from typing import List
from FactoryMethodZoo.AnimalFactory import AnimalFactory
from FactoryMethodZoo.Lion      import Lion
from FactoryMethodZoo.Elephant  import Elephant
from FactoryMethodZoo.Penguin   import Penguin
from FactoryMethodZoo.WhiteBear import WhiteBear

class TorontoAnimalFactory(AnimalFactory):
    def create_lion(self):        return Lion()
    def create_elephant(self):    return Elephant()
    def create_penguin(self):     return Penguin()
    def create_white_bear(self):  return WhiteBear()
    def create_grizzly_bear(self): return None
    def create_moose(self):        return None

    def create_all_animals(self) -> List:
        return [self.create_lion(),
                self.create_elephant(),
                self.create_penguin(),
                self.create_white_bear()]