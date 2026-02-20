student_marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "History": 92
}

subject = input("Enter the subject to get the marks: ").title()

if subject in student_marks:
    print(f"The marks for {subject} are: {student_marks[subject]}")
else:
    print("Subject not found in the student marks dictionary.")