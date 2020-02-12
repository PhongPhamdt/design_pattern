class Employee(object):
    def work(self):
        pass
    

class Manager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


class Developer(Employee):
    def __init__(self):
        print("developer added")


class Designer(Employee):
    def __init__(self):
        print("designer added")


class Testers(Employee):
    def __init__(self):
        print("tester added")


if __name__ == "__main__":
    a = Manager()
    a.add_employee(Developer())
    a.add_employee(Designer())
