# WAP to count the number of students with the "A" grade in the following tuple:
students = ("John", "Alice", "Bob", "Eve", "Charlie")
grades = ("A", "B", "A", "C", "A")

# Count the number of students with "A" grade
count_a_grade = grades.count("A")
print(f"The number of students with 'A' grade is: {count_a_grade}") # Output: The number of students with 'A' grade is: 3 

# what is f in the print statement? The "f" in the print statement indicates that it is an f-string, which is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. In this case, {count_a_grade} will be replaced with the value of the variable count_a_grade when the string is printed.
