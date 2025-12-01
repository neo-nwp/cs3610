from typing import List
from org_node import OrgNode

class Department(OrgNode):
    def __init__(self, name: str):
        self.name = name
        self._children: List[OrgNode] = []

    def add(self, node: OrgNode) -> None:
        self._children.append(node)

    def remove(self, node: OrgNode) -> None:
        self._children.remove(node)

    def get_total_salary(self) -> float:
        return sum(child.get_total_salary() for child in self._children)

    def do_operation(self, task: str) -> str:
        results = [f"Department {self.name} coordinated task: '{task}'"]
        for child in self._children:
            results.append(child.do_operation(task))
        return "\n".join(results)