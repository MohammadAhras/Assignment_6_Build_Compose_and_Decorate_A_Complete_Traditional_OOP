class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_department_details(self):
        print(f"Department: {self.department_name}")
        for employee in self.employees:
            employee.display_details()
            print("------------------------")

employee1 = Employee("Akram", "E001")
employee2 = Employee("Alishba", "E009")

hr_dept = Department("HR")
hr_dept.add_employee(employee1)

it_dept = Department("IT")
it_dept.add_employee(employee2)

# Both departments can access the same employee
hr_dept.display_department_details()
it_dept.display_department_details()

#Employees exists independently of department
employee2.display_details()