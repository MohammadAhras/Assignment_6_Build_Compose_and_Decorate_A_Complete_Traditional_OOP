class Employee:
    def __init__(self, name, salry, ssn):
        self.name = name # public
        self._salary = salry #protected
        self.__ssn = ssn  #private


emp = Employee("AHRAS", 50000, "48291919190010")

print(emp.name)
print(emp._salary)
print(emp.__ssn)

