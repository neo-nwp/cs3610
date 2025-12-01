from abc import ABC, abstractmethod
from ipayment_processor import IPaymentProcessor   

class Employee(ABC):
    def __init__(self, name: str, processor: IPaymentProcessor):
        self.name = name
        self.processor = processor

    @abstractmethod
    def calculate_pay(self) -> float:
        raise NotImplementedError

    def process_payment(self) -> str:
        amount = self.calculate_pay()
        return self.processor.pay(amount,self.name)

# refined abstractions
class HourlyEmployee(Employee):
    def __init__(self, name: str, hours: float, rate: float, processor: IPaymentProcessor):
        super().__init__(name, processor)
        self.hours = hours
        self.rate = rate

    def calculate_pay(self) -> float:
        return self.hours * self.rate

class SalariedEmployee(Employee):
    def __init__(self, name: str, monthly_salary: float, processor: IPaymentProcessor):
        super().__init__(name, processor)
        self.monthly_salary = monthly_salary

    def calculate_pay(self) -> float:
        return self.monthly_salary

class Contractor(Employee):
    def __init__(self, name: str, project_pay: float, processor: IPaymentProcessor):
        super().__init__(name, processor)
        self.project_pay = project_pay

    def calculate_pay(self) -> float:
        return self.project_pay