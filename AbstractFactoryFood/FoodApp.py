from typing import List, Dict, Type
from AbstractFactoryFood.IProduct import IProduct
from AbstractFactoryFood.IProductFactory import IProductFactory
from AbstractFactoryFood.VegProductFactory import VegProductFactory
from AbstractFactoryFood.NonVegProductFactory import NonVegProductFactory

class FoodApp:
    AvailableFood: Dict[str, Type[IProductFactory]] = {
    "VegBurger":  VegProductFactory,
    "VegPizza":   VegProductFactory,
    "VegNoodles": VegProductFactory,
    "NonVegBurger": NonVegProductFactory,
    "NonVegPizza":  NonVegProductFactory,
    "NonVegNoodles": NonVegProductFactory,
}

    def makeOrder(self, prodNames: List[str]) -> List[IProduct]:
        order = []
        for name in prodNames:
            factory_class = self.AvailableFood.get(name)
            if not factory_class:
                print(f"Error: Product '{name}' is not available.")
                continue
            factory = factory_class()
            if name == "VegBurger":
                item = factory.createBurger(5, 250, "Delicious veg patty")
            elif name == "VegPizza":
                item = factory.createPizza(8, 400, "Cheesy veg delight", "Medium")
            elif name == "NonVegBurger":
                item = factory.createBurger(7, 350, "Juicy beef patty")
            elif name == "NonVegPizza":
                item = factory.createPizza(10, 500, "Pepperoni & chicken", "Large")
            elif name == "VegNoodles":
                item = factory.createNoodles(6, 300, "Fresh veg hakka noodles")
            elif name == "NonVegNoodles":
                item = factory.createNoodles(8, 450, "Chicken hakka noodles")
            else:
                continue
            order.append(item)
        return order

    #  outputs price, desc, size, calories for every item
    def getOrderDescription(self, products: List[IProduct]) -> str:
        lines = []
        for p in products:
            base = f"{p.get_Description()} - ${p.get_Price()} | Calories: {p.get_Calories()}"
            # add size only for pizzas
            if hasattr(p, 'get_Size'):
                base += f" | Size: {p.get_Size()}"
            lines.append(base)
        return "\n".join(lines)