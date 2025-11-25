from typing import List
from FactoryMethodZoo.AnimalFactory import AnimalFactory
from FactoryMethodZoo.GrizzlyBear import GrizzlyBear
from FactoryMethodZoo.Moose       import Moose
from FactoryMethodZoo.Penguin     import Penguin

class CalgaryAnimalFactory(AnimalFactory):
    def create_grizzly_bear(self): return GrizzlyBear()
    def create_moose(self):        return Moose()
    def create_penguin(self):      return Penguin()
    def create_lion(self):         return None
    def create_elephant(self):     return None
    def create_white_bear(self):   return None

    def create_all_animals(self) -> List:
        return [self.create_grizzly_bear(),
                self.create_moose(),
                self.create_penguin()]