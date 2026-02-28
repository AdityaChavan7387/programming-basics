# Create Student Class that takes name & marks of 3 subjects as arguments in constructor. Than create a method to print the average marks of the student.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)
# Example usage:
student1 = Student("Alice", [85, 90, 78]) # Create an instance of the Student class with name "Alice" and marks [85, 90, 78]
print(f"{student1.name}'s average marks: {student1.average_marks()}")  # Print the average marks of student1 using the average_marks method
student2 = Student("Bob", [92, 88, 95])
print(f"{student2.name}'s average marks: {student2.average_marks()}")