from FactoryMethodZoo.TorontoZoo import TorontoZoo
from FactoryMethodZoo.CalgaryZoo import CalgaryZoo

def main():
    # Toronto Zoo
    toronto = TorontoZoo()
    print(toronto.get_itinerary())
    print("Animal sounds:", toronto.get_animal_sounds())
    print()

    # Calgary Zoo
    calgary = CalgaryZoo()
    print(calgary.get_itinerary())
    print("Animal sounds:", calgary.get_animal_sounds())

if __name__ == "__main__":
    main()