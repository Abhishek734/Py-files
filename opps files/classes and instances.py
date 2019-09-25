# class (blueprint)

class Employee:
    def __init__(self,first,last,pay):                 # constructor self == instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self): # dont forget self
        return '{} {}'.format(self.first,self.last)

# instances
emp_1 = Employee("Avinas","kumar",50000)  # self passed automatically
emp_2 = Employee("deepa","kumari",40000)

print(emp_1)
# print(emp_2)

# emp_1.first = "Abhi"
# emp_1.last = "prasad"
# emp_1.email = "Abhi.prasad@gmail.com"
# emp_1.pay = 700000

# emp_2.first = "Anu"
# emp_2.last = "kumari"
# emp_2.email = "Anu.kumar2@gmail.com"
# emp_2.pay = 400000

# print(emp_1.email)
# print(emp_2.email)
print(emp_1.fullname())
# print(emp_2.fullname())

print(Employee.fullname(emp_1))
