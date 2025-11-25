from BuilderCustomer.ICustomerBuilder import ICustomerBuilder
from BuilderCustomer.CustomerProfile import CustomerProfile
from BuilderCustomer.ContactDetail import ContactDetail

class MobileAppBuilder(ICustomerBuilder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = CustomerProfile()

    def add_first_name(self, name: str) -> None:
        self._product.add_detail(ContactDetail("First Name", name))

    def add_middle_name(self, name: str) -> None:
        pass  # mobile does not collect this

    def add_last_name(self, name: str) -> None:
        self._product.add_detail(ContactDetail("Last Name", name))

    def add_primary_email(self, email: str) -> None:
        self._product.add_detail(ContactDetail("Primary Email", email))

    def add_secondary_email(self, email: str) -> None:
        pass  # mobile does not collect this

    def add_primary_mobile(self, number: str) -> None:
        self._product.add_detail(ContactDetail("Primary Mobile", number))

    def add_secondary_mobile(self, number: str) -> None:
        pass  # mobile does not collect this

    def get_product(self) -> CustomerProfile:
        result = self._product
        self.reset()
        return result