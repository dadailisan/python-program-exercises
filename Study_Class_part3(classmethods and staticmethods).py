#Youtube channel of Corey Schafer

#Python Object-Oriented Programming

#Regular Methods: takes instances as first argument(self)
#Class method: takes class as first argument(self)
#Static Method: Doesn't pass instances(self) or class(cls) as first argument. its a regular
    #function inside a class.

class Employee:
    #num_of_emps and raise_amt are class variables
    num_of_emps = 0
    raise_amt = 1.04
    #def are called functions or methods if inside a class
    #Regular Methods
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
       self.pay = int(self.pay * self.raise_amt)
#Class Method
#if we want to change the class variable raise_amt to other multiplier
#to check run this code below:
##emp_1 = Employee('Corey', 'Schafer', 50000)
##emp_2 = Employee('Test', 'User', 60000)
##Employee.set_raise_amt = 1.05)
##print(Employee.raise_amt)
##print(emp_1.raise_amt)
##print(emp_2.raise_amt)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

#in case the input have '-' in betweeen of first,last,pay
#to check run this code:
##emp_str_1 = 'John-Joe-70000'
##emp_str_2 = 'Steve-Smith-30000'
##new_emp_1 = Employee.from_string(emp_str_1)
##print(new_emp_1.email)
##print(new_emp_1.pay)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

#Static Method
#checking if it is a work day. using weekday method where in 0==monday,
#1==tuesday and so on. our static method checks if it is sunday(6) or saturday(5)
#to check run this code:
##import datetime
##my_date = datetime.date(2018, 2, 21)
##print(Employee.is_workday(my_date))
    @staticmethod
    def is_workday(day): #doesn't take self or cls
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

