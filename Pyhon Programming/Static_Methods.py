# In This we will learn about Static Methods in Python

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @staticmethod
    def printgood(string):
        print("This is good " + string)
harry = Employee("Harry", 255, "Instructor")
harry.printgood("Python")   
# We can also call the static method using the class name
Employee.printgood("Python")

