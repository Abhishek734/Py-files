# Property_decorators(getter-setters-deleters).py
class Employee:

    def __init__(self, first, last): # __init__ dunder methods(__vv__)
        self.first = first
        self.last = last

    @property # setting function as an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter # setter example
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter # deleter example
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee("john", "smith")
# print(emp_1.first)
# print(emp_1.email)

emp_1.fullname = "Corey Sachafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
