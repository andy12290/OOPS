# This is related to OOP in python.


class Employee:

    # Class variable to access the every method

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# output

Ani = Employee('Aniket', 'Kale', '250')
print(Ani.fullname())

#
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_2.last)
