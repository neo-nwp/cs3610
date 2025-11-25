from __future__ import annotations   # allows forward refs
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BuilderCustomer.ContactDetail import ContactDetail

class CustomerProfile:
    def __init__(self) -> None:
        self._details: list[ContactDetail] = []

    def add_detail(self, detail: ContactDetail) -> None:
        self._details.append(detail)

    def show(self) -> str:
        if not self._details:
            return "Empty Customer"
        return "\n".join(str(d) for d in self._details)