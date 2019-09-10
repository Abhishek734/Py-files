#class variables.py
#class varibales are shared among all the instances of the class

class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay):                 # constructor self == instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self): # dont forget self
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)
# instances
emp_1 = Employee("Avinas","kumar",50000)  # self passed automatically
emp_2 = Employee("deepa","kumari",40000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print(emp_1.__dict__)
print(Employee.__dict__)
