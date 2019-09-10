# inheritence.py
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developers(Employee):                                 # simple inherit Employee class
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)                    # wow super()
        # Employee.__init__(Self, first,last,pay)           # does the same
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first,last,pay)                    # wow super()
        # Employee.__init__(Self, first,last,pay)           # does the same
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->",emp.fullname())

dev_1 = Developers('Corey', 'Schafer', 50000,"python")
dev_2 = Developers('Test', 'Employee', 60000,"java")

mgr_1 = Manager("sue", "smith", 900000,[dev_1])

# is instance
print(isinstance(mgr_1, Manager)) # True
print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developers)) # false
# issubclass --> to check subclass
print(issubclass(Developers, Employee))  #True
print(issubclass(Manager, Employee)) # True
print(issubclass(Manager,Developers)) # False
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emp()


# help(Developers)

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
