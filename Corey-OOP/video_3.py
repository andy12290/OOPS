class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 and day.weekday == 6:
            return False
        else:
            return True
# output


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.set_raise(1.05)


print(emp_1.num_of_emps)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
