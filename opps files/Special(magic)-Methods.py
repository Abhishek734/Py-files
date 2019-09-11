# Special(magic)-Methods.py
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay): # __init__ dunder methods(__vv__)
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return 'Employee("{}","{}","{}")'.format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self, other):            # just for example
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Avinas","kumar",50000)
emp_2 = Employee("deepa","kumari",40000)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__str__())

## these two methods allow us to how outputs are printed and displayed.

# arithmetic magic methods
# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__("a","b"))

#-------------------------------------------------------------------
# print(emp_1 + emp_2)
#------------------------
# print(len("test"))
# print("test".__len__())
#------------------------

print(len(emp_1))
