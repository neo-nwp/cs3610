from grinder import Grinder
from apple_juice import AppleJuice
from orange_juice import OrangeJuice


def main() -> None:
    grinder = Grinder()

    print("=== Apple Juice ===")
    grinder.process(AppleJuice())

    print("\n=== Orange Juice ===")
    grinder.process(OrangeJuice())


if __name__ == "__main__":
    main()
