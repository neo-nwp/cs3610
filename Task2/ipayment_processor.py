from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float, name: str) -> str:
        raise NotImplementedError