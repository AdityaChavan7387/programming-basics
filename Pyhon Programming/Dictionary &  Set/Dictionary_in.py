Student = {  #Creating a dictionary named Student
    "name": 'John',
    "age": 20,
    "major": 'Computer Science',
    "CGPA": 3.5,
}

Student["surname"] = "Doe" # Adding a new key-value pair to the Student dictionary. The key is "surname" and the value is "Doe".
print(Student)

print(type(Student)) #This will print the type of the variable Student, which is <class 'dict'>, indicating that it is a dictionary.


# Dictionaries are mutable, but we cannot have duplicate keys. If we try to add a key that already exists, it will overwrite the existing value.