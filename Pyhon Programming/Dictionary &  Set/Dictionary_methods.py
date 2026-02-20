# In this we will see some of the methods or functions of dictionary.

student_marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "History": 92
}

# 1. get() method: This method is used to retrieve the value associated with a specific key in the dictionary. It takes the key as an argument and returns the corresponding value. If the key is not found, it returns a default value (which can be specified as a second argument) or None if no default value is provided.
subject = input("Enter the subject to get the marks: ").title()
marks = student_marks.get(subject, "Subject not found in the student marks dictionary.")
print(f"The marks for {subject} are: {marks}")  

# 2. keys() method: This method returns a view object that displays a list of all the keys in the dictionary.
print("Subjects available in the student marks dictionary:")
for subject in student_marks.keys():
    print(subject)

# 3. values() method: This method returns a view object that displays a list of all the values in the dictionary.
print("Marks for all subjects in the student marks dictionary:")
for marks in student_marks.values():
    print(marks)

# 4. items() method: This method returns a view object that displays a list of key-value pairs in the dictionary as tuples.
print("Subjects and their corresponding marks in the student marks dictionary:")    
for subject, marks in student_marks.items():
    print(f"{subject}: {marks}")

# 5. update() method: This method is used to update the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs. If a key already exists, its value will be updated.
new_marks = {
    "Math": 88,  # Updating existing key
    "Geography": 80  # Adding new key
}
student_marks.update(new_marks)
print("Updated student marks dictionary:")
for subject, marks in student_marks.items():
    print(f"{subject}: {marks}")

# 6. pop() method: This method is used to remove a key-value pair from the dictionary based on the key. It takes the key as an argument and returns the value associated with that key. If the key is not found, it raises a KeyError or returns a default value if provided.
removed_marks = student_marks.pop("Science", "Subject not found in the student marks dictionary.")  
print(f"Removed marks for Science: {removed_marks}")
print("Student marks dictionary after removing Science:")
for subject, marks in student_marks.items():
    print(f"{subject}: {marks}")

# 7. clear() method: This method is used to remove all key-value pairs from the dictionary, leaving it empty.
student_marks.clear()
print("Student marks dictionary after clearing all entries:")
print(student_marks)  # This will print an empty dictionary {}  

