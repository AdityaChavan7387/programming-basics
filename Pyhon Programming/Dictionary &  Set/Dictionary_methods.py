# I wrote the code but it was messy so i will take help of AI for this one and make it simple and easy to understand.
# A dictionary stores data in the form of:
# key : value
# Here, subject is the key and marks are the value.

student_marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "History": 92
}

# -------------------------------
# 1. get() → Find value using key
# -------------------------------
# It safely gets the value of a key.
# If the key is not found, it shows a message instead of giving an error.

subject = input("Enter subject name: ").title()

marks = student_marks.get(subject, "Subject not found")

print("Marks:", marks)


# -------------------------------
# 2. keys() → Show all keys
# -------------------------------
print("\nAll Subjects:")
for subject in student_marks.keys():
    print(subject)


# -------------------------------
# 3. values() → Show all values
# -------------------------------
print("\nAll Marks:")
for marks in student_marks.values():
    print(marks)


# -------------------------------
# 4. items() → Show key and value together
# -------------------------------
print("\nSubjects and Marks:")
for subject, marks in student_marks.items():
    print(subject, ":", marks)


# -------------------------------
# 5. update() → Add or change values
# -------------------------------
# If key exists → it changes the value
# If key does not exist → it adds new key

student_marks.update({
    "Math": 88,        # Changed value
    "Geography": 80    # New subject added
})

print("\nAfter update:")
for subject, marks in student_marks.items():
    print(subject, ":", marks)


# -------------------------------
# 6. pop() → Remove one item
# -------------------------------
# Removes the key and returns its value

removed = student_marks.pop("Science", "Not found")

print("\nRemoved Science marks:", removed)

print("After removing Science:")
for subject, marks in student_marks.items():
    print(subject, ":", marks)


# -------------------------------
# 7. clear() → Remove everything
# -------------------------------
student_marks.clear()

print("\nAfter clearing dictionary:")
print(student_marks)   # Output: {}