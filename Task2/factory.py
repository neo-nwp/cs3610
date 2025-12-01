from typing import Dict, Type
from ipayment_processor import IPaymentProcessor          
from payment_processor import (
    BankTransferProcessor,
    ChequeProcessor,
    DigitalWalletProcessor,
)

class PaymentProcessorFactory:
    _processors: Dict[str, Type[IPaymentProcessor]] = {
        "bank transfer": BankTransferProcessor,
        "cheque": ChequeProcessor,
        "digital wallet": DigitalWalletProcessor,
    }

    @staticmethod
    def create_processor(payment_type: str) -> IPaymentProcessor:
        processor_cls = PaymentProcessorFactory._processors.get(payment_type.lower())
        if not processor_cls:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_cls()