from FactoryMethodZoo.IZoo import IZoo
from FactoryMethodZoo.Itinerary import Itinerary
from FactoryMethodZoo.CalgaryAnimalFactory import CalgaryAnimalFactory
from FactoryMethodZoo.AnimalFactory import AnimalFactory

class CalgaryZoo(IZoo):
    def _create_itinerary(self) -> Itinerary:
        return Itinerary("Welcome to the Calgary Zoo! Our Itinerary: 1) Penguin Plunge. 2) Wild Canada")

    def _create_animal_factory(self) -> AnimalFactory:
        return CalgaryAnimalFactory()