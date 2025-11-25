from AbstractFactoryFood.FoodApp import FoodApp

def main():
    app = FoodApp()
    for label, names in [
    ("VEGETARIAN",   ["VegBurger", "VegPizza", "VegNoodles"]),
    ("NON-VEGETARIAN", ["NonVegBurger", "NonVegPizza", "NonVegNoodles"]),
    ("MIXED",          ["VegBurger", "NonVegNoodles"])
        ]:
        print(f"=== {label} ORDER ===")
        order = app.makeOrder(names)
        print(app.getOrderDescription(order), end="\n\n")

if __name__ == "__main__":
    main()