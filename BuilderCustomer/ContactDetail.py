class ContactDetail:
    def __init__(self, detail_type: str, value: str):
        self.detail_type = detail_type
        self.value = value

    def __str__(self) -> str:
        return f"{self.detail_type}: {self.value}"