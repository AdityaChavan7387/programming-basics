# Type Conversion

a = 2  # a is an integer
b = 3.14 # b is a float

# implicit type conversion (type coercion)
sum = a + b  # 3.0 + 3.14 = 6.14
print(sum)  # Output: 6.14

# Type casting
c = int("2")  # converting string "3" to integer 3 and we can assign a type to a variable on our own only for values that can be converted to that type. For example, we cannot convert a string "hello" to an integer.
d = 4.14
print(type(c))  # Output: <class 'int'> 
print(c + d)  # Output: 6.14