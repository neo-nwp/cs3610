from juice import Juice


class Grinder:
    """
    Client code: depends only on the abstraction (Juice).
    It knows nothing about the concrete subclasses.
    """
    def process(self, j: Juice) -> None:
        j.makeJuiceFromMe()
