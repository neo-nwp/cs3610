from abc import ABC, abstractmethod
from FactoryMethodZoo.Itinerary import Itinerary
from FactoryMethodZoo.AnimalFactory import AnimalFactory
from typing import List

class IZoo(ABC):
    def __init__(self):
        self._animals: List[IAnimal] = []
        self._itinerary = self._create_itinerary()
        factory = self._create_animal_factory()
        self._animals = factory.create_all_animals()

    @abstractmethod
    def _create_itinerary(self) -> Itinerary: ...
    @abstractmethod
    def _create_animal_factory(self) -> AnimalFactory: ...

    # read-only helpers
    def get_itinerary(self) -> str:
        return str(self._itinerary)

    def get_animal_sounds(self) -> List[str]:
        return [animal.say() for animal in self._animals]