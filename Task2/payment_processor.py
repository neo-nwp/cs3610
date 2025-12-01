from ipayment_processor import IPaymentProcessor

class BankTransferProcessor(IPaymentProcessor):
    def pay(self, amount: float, name: str) -> str:
        return f"{name} -> Paid ${amount:.2f} via Bank Transfer"

class ChequeProcessor(IPaymentProcessor):
    def pay(self, amount: float, name: str) -> str:
        return f"{name} -> Paid ${amount:.2f} by Cheque"

class DigitalWalletProcessor(IPaymentProcessor):
    def pay(self, amount: float, name: str) -> str:
        return f"{name} -> Paid ${amount:.2f} using Digital Wallet"