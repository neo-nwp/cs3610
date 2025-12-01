from abc import ABC, abstractmethod

class OrgNode(ABC):
    """Component interface for both leaves and composites."""
    @abstractmethod
    def get_total_salary(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def do_operation(self, task: str) -> str:
        """Return a string describing work done by this node."""
        raise NotImplementedError