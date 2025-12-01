from employee import Employee
from department import Department

class Company:
    @staticmethod
    def build_sample() -> Department:
        # Leaf nodes
        alice = Employee("Alice", 5000)
        bob   = Employee("Bob", 4000)
        carol = Employee("Carol", 4500)
        dave  = Employee("Dave", 3000)

        # Departments
        dev_team = Department("Development")
        dev_team.add(alice)
        dev_team.add(bob)

        qa_team = Department("QA")
        qa_team.add(carol)
        qa_team.add(dave)

        engineering = Department("Engineering")
        engineering.add(dev_team)
        engineering.add(qa_team)

        return engineering

    @staticmethod
    def run_demo() -> None:
        org = Company.build_sample()

        # Uniform operations
        print("Total company salary:", org.get_total_salary())
        print("\nAssigning task:")
        print(org.do_operation("Deploy new release"))

if __name__ == "__main__":
    Company.run_demo()