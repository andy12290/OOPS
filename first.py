# classess and Method means function inside classess

# Employee means each has different account and name email

class Employee:
    pass

emp_1 =  Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
emp_1.first = 'Aniket'
emp_1.last = 'Kale'

emp_2.first = 'Sachin'
emp_2.last = 'Tendulkar'
# so we have different memory location for the class
print(emp_2.first)



# classess with constructor

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '@company.com'

    def fullname(self):
        return('{} {}'.format(self.first, self.last))

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1.last)

print(emp_2.first)
print(emp_1.fullname())# why () its method than attributes
