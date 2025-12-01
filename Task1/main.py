from adapters import (
    TaxCalculator, AccountingModule, CreditAuthorizationService,
    CSVAdapter, XMLAdapter, CustomAdapter
)
from forcasting_module import ForecastingModule

def main():
    # Create external API objects
    tax_calc = TaxCalculator()
    acc_module = AccountingModule()
    credit_service = CreditAuthorizationService()

    # Create adapters
    csv_adapter = CSVAdapter(tax_calc)
    xml_adapter = XMLAdapter(acc_module)
    custom_adapter = CustomAdapter(credit_service)

    # Forecasting module
    sources = [csv_adapter, xml_adapter, custom_adapter]
    forecasting = ForecastingModule(sources)
    forecasting.process_data()

if __name__ == "__main__":
    main()