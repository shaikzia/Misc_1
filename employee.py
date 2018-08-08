class Employee:
    employees = ''

    def __init__(self, employees={}):
            self.employees = employees

    def set_employees(self, employees):
        self.employees = employees

    def get_employees(self):
        return  self.employees

employees = ['Faiz', 'Zairah', 'Saad', 'Sajida', 'Zia']
zia = Employee()
zia.set_employees(employees)
print(zia.get_employees())

