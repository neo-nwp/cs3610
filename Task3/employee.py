from org_node import OrgNode

class Employee(OrgNode):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def get_total_salary(self) -> float:
        return self.salary

    def do_operation(self, task: str) -> str:
        return f"Employee {self.name} executed task: '{task}'"