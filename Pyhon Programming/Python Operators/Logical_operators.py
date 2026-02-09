# Logical Operators in Python

print(not True)  # Output: False
print(not False)  # Output: True

print(True and True)  # Output: True
print(True and False)  # Output: False
print(False and True)  # Output: False
print(False and False)  # Output: False

print(True or True)  # Output: True
print(True or False)  # Output: True
print(False or True)  # Output: True
print(False or False)  # Output: False

# Example of using logical operators in a condition
a = 50
b = 30
print(not (a > b))  # Output: False
print(not (a < b))  # Output: True

val1 = True
val2 = True
val3 = False
val4 = False
print("Using And Operator : ", val1 and val2)  # Output: True
print("Using And Operator : ", val1 and val3) # Output: False

print("Using OR Operator : ", val1 or val3)  # Output: True
print("Using OR Operator : ", val3 or val4)  # Output: False