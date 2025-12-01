import json
import csv
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

# Target interface expected by Forecasting Module
class JSONTarget(ABC):
    @abstractmethod
    def get_json_data(self) -> dict:
        pass

# External APIs
class TaxCalculator:
    def get_csv_data(self) -> str:
        # CSV data
        return "tax_type,income,tax_due\nfederal,50000,5000"

class AccountingModule:
    def get_xml_data(self) -> str:
        # XML data
        return "<account><income>50000</income><expenses>20000</expenses></account>"

class CreditAuthorizationService:
    def get_custom_data(self) -> dict:
        # custom format
        return {"credit_score": 720, "approved": True}

# Adapters
class CSVAdapter(JSONTarget):
    def __init__(self, tax_calc: TaxCalculator):
        self.tax_calc = tax_calc

    def get_json_data(self) -> dict:
        csv_data = self.tax_calc.get_csv_data()
        reader = csv.DictReader(csv_data.splitlines())
        return [row for row in reader]

class XMLAdapter(JSONTarget):
    def __init__(self, acc_module: AccountingModule):
        self.acc_module = acc_module

    def get_json_data(self) -> dict:
        xml_data = self.acc_module.get_xml_data()
        root = ET.fromstring(xml_data)
        return {child.tag: child.text for child in root}

class CustomAdapter(JSONTarget):
    def __init__(self, credit_service: CreditAuthorizationService):
        self.credit_service = credit_service

    def get_json_data(self) -> dict:
        return self.credit_service.get_custom_data()