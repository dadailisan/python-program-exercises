#Youtube channel of Corey Schafer

#Python Object-Oriented Programming

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

##print(emp_1)
##print(emp_2)
##
##emp_1.first = 'Corey'
##emp_1.last = 'Schafer'
##emp_1.email = 'Corey.Schafer@company.com'
##emp_1.pay = 50000
##
##emp_2.first = 'Test'
##emp_2.last = 'User'
##emp_2.email = 'Test.User@company.com'
##emp_2.pay = 60000
#test to check if the class will give the emp_1 and emp_2 emails
#print(emp_1.email)
#print(emp_2.email)

#manually print the first and last name of the employee
#print('{} {}'.format(emp_1.first, emp_1.last))

#after adding the def fullname function/method on our class.
#print(emp_1.fullname())

#printing the fullname using the class. This is what actually happens when you rung emp_1.fullname()

#print(Employee.fullname(emp_1))

#this shows the functions/variables for the Class
#print(Employee.__dict__)

#test if the num_of_emps work
print(Employee.num_of_emps)
emp_3 = Employee('Doms', 'Dailisan', 55000)
print(Employee.num_of_emps)
