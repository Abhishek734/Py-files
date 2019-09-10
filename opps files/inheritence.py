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


dev_1 = Developers('Corey', 'Schafer', 50000,"python")
dev_2 = Developers('Test', 'Employee', 60000,"java")

# help(Developers)

print(dev_1.email)
print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
