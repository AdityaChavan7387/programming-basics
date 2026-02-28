# In This we will see how to use constructor in python and how it is used in class and object
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}") # what is mean by f in print statement # The 'f' in the print statement indicates that it is an f-string, which is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. In this case, the values of self.name, self.age, and self.salary will be evaluated and inserted into the string at the respective positions when the display method is called.
# Creating an object of the Employee class
emp1 = Employee("John Doe", 30, 50000)
emp1.display()
# Output: Name: John Doe, Age: 30, Salary: 50000

# In this example, we have defined a class called Employee with a constructor method __init__. The constructor takes three parameters: name, age, and salary. When we create an object of the Employee class, we pass the values for these parameters, and the constructor initializes the object's attributes accordingly. The display method is then used to print the employee's details.
