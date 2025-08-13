class Employee:
    def get_details(self, name, department, role, salary):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary

    def show_details(self):
        print(f"name of the employee:{self.name}\nDepartment:{self.department}\nrole:{self.role}\nsalary:{self.salary}")

e = Employee()
e.get_details('Rishi', 'finance', 'analyist', 25000 )
e.show_details()