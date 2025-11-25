from BuilderCustomer.ICustomerBuilder import ICustomerBuilder
from BuilderCustomer.CustomerProfile import CustomerProfile
from BuilderCustomer.ContactDetail import ContactDetail

class WebAppBuilder(ICustomerBuilder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = CustomerProfile()

    def add_first_name(self, name: str) -> None:
        self._product.add_detail(ContactDetail("First Name", name))

    def add_middle_name(self, name: str) -> None:
        self._product.add_detail(ContactDetail("Middle Name", name))

    def add_last_name(self, name: str) -> None:
        self._product.add_detail(ContactDetail("Last Name", name))

    def add_primary_email(self, email: str) -> None:
        self._product.add_detail(ContactDetail("Primary Email", email))

    def add_secondary_email(self, email: str) -> None:
        self._product.add_detail(ContactDetail("Secondary Email", email))

    def add_primary_mobile(self, number: str) -> None:
        self._product.add_detail(ContactDetail("Primary Mobile", number))

    def add_secondary_mobile(self, number: str) -> None:
        self._product.add_detail(ContactDetail("Secondary Mobile", number))

    def get_product(self) -> CustomerProfile:
        # ready to build next customer
        result = self._product
        self.reset()
        return result