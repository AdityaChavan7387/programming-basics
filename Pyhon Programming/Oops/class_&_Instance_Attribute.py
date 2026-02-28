# in this we will see the difference between class and instance attribute

class Employee:
    company = "Google"  # this is a class attribute

    def __init__(self, name, salary):
        self.name = name  # this is an instance attribute
        self.salary = salary  # this is an instance attribute

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)   
print(emp1.company)  # Output: Google
print(emp2.company)  # Output: Google
print(emp1.name)     # Output: Alice
print(emp2.name)     # Output: Bob

# Now if we change the class attribute
Employee.company = "Microsoft"
print(emp1.company)  # Output: Microsoft
print(emp2.company)  # Output: Microsoft    
# But if we change the instance attribute
emp1.name = "Charlie"
print(emp1.name)     # Output: Charlie
print(emp2.name)     # Output: Bob

