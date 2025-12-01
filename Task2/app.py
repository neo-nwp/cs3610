from factory import PaymentProcessorFactory
from employee import HourlyEmployee, SalariedEmployee, Contractor

class HRApp:
    AvalPaymentMethods = ["bank transfer", "cheque", "digital wallet"]

    @staticmethod
    def run():
        bank   = PaymentProcessorFactory.create_processor("bank transfer")
        cheque = PaymentProcessorFactory.create_processor("cheque")
        digital= PaymentProcessorFactory.create_processor("digital wallet")

        employees = [
            SalariedEmployee("Alice", 5000.0, bank),
            HourlyEmployee("Bob", 160, 25.0, cheque),
            Contractor("Carol", 12000.0, digital),
        ]

        for emp in employees:
            print(emp.process_payment())

if __name__ == "__main__":
    HRApp.run()