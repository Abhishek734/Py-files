#classmethods and staticmethods.py
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):                 # constructor self == instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1                       # not self as we don't have to change it for every instances

    def fullname(self): # dont forget self
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount): # cls class Variable //self for instance varibale
        cls.raise_amount = amount

    @classmethod # new constructor //class methods as alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

# instances

emp_1 = Employee("Avinas","kumar",50000)  # self passed automatically
emp_2 = Employee("deepa","kumari",40000)

# Employee.set_raise_amount(1.05) # set_raise_amount --> class method {== Employee.raise_amount = 1.05}

# # emp_1.set_raise_amount(1.05) # same results

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)


