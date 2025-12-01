from typing import List
from adapters import JSONTarget

class ForecastingModule:
    def __init__(self, sources: List[JSONTarget]):
        self.sources = sources
        
    def process_data(self):
        for source in self.sources:
            json_data = source.get_json_data()
            print("Processing JSON data:", json_data)