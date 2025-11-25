from BuilderCustomer.CustomerDirector import CustomerDirector
from BuilderCustomer.WebAppBuilder import WebAppBuilder
from BuilderCustomer.MobileAppBuilder import MobileAppBuilder

def main():
    director = CustomerDirector()

    print("=== WEB APP CUSTOMER ===")
    web = director.construct_customer(
        WebAppBuilder(),
        first_name="Alice", middle_name="Marie", last_name="Johnson",
        primary_email="alice@example.com", secondary_email="alice@work.com",
        primary_mobile="+1234567890", secondary_mobile="+0987654321"
    )
    print(web.show())
    print()

    print("=== MOBILE APP CUSTOMER ===")
    mobile = director.construct_customer(
        MobileAppBuilder(),
        first_name="Bob", middle_name="IGNORED", last_name="Smith",
        primary_email="bob@example.com", secondary_email="ignored",
        primary_mobile="+1122334455", secondary_mobile="ignored"
    )
    print(mobile.show())

if __name__ == "__main__":
    main()