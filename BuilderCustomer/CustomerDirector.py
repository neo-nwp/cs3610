from BuilderCustomer.ICustomerBuilder import ICustomerBuilder

class CustomerDirector:
    def construct_customer(self,
                           builder: ICustomerBuilder,
                           first_name: str,
                           middle_name: str,
                           last_name: str,
                           primary_email: str,
                           secondary_email: str,
                           primary_mobile: str,
                           secondary_mobile: str):
        builder.add_first_name(first_name)
        builder.add_middle_name(middle_name)
        builder.add_last_name(last_name)
        builder.add_primary_email(primary_email)
        builder.add_secondary_email(secondary_email)
        builder.add_primary_mobile(primary_mobile)
        builder.add_secondary_mobile(secondary_mobile)
        return builder.get_product()