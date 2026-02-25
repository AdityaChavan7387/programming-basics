# Create A New File "Practice.txt" using python. Add The Following Data in it :

# Hi Everyone,
# We Are learning File I/O in Python.
# using Java
# I like programming.

with open("Practice.txt", "w") as file:
    file.write("Hi Everyone,\n")
    file.write("We Are learning File I/O in Python.\n")
    file.write("using Java\n")
    file.write("I like programming.\n")