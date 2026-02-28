# In This we will learn about class and objects in python

# A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# An object is an instance of a class. It is created from the class and has all the attributes and methods defined in the class.
# Here is an example of a class and an object in Python:

class Student:
    name = "John"
    age = 20
# Creating an object of the Student class
student1 = Student()
# Accessing the attributes of the student1 object
print(student1.name)  # Output: John
print(student1.age)   # Output: 20``

# another example of a class and an object in Python:

class Car:
    color = "Red"
    model = "Toyota"
# Creating an object of the Car class
car1 = Car()
# Accessing the attributes of the car1 object
print(car1.color)  # Output: Red
print(car1.model)  # Output: Toyota