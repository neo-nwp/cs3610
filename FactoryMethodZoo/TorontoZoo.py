from FactoryMethodZoo.IZoo import IZoo
from FactoryMethodZoo.Itinerary import Itinerary
from FactoryMethodZoo.TorontoAnimalFactory import TorontoAnimalFactory
from FactoryMethodZoo.AnimalFactory import AnimalFactory

class TorontoZoo(IZoo):
    def _create_itinerary(self) -> Itinerary:
        return Itinerary("Welcome to the Toronto Zoo! Our Itinerary: 1) African Savanna. 2) Tundra Trek")

    def _create_animal_factory(self) -> AnimalFactory:
        return TorontoAnimalFactory()