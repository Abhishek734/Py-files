# class (blueprint)

class Employee:
    pass

# instances
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = "Abhi"
emp_1.last = "prasad"
emp_1.email = "Abhiprasad@gmail.com"
emp_1.pay = 700000

emp_2.first = "Anu"
emp_2.last = "kumari"
emp_2.email = "Anukumar2@gmail.com"
emp_2.pay = 400000

print(emp_1.email)
print(emp_2.email)
