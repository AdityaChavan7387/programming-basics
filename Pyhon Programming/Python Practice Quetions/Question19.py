# WAP to enter marks of 3 subjects from the user 
# and store them in a dictionary.
# Start with an empty dictionary & add one by one.
# Use subject name as key & marks as value.

# Start with empty dictionary
marks = {}

# Loop to take input for 3 subjects
for i in range(3):
    subject = input("Enter subject name: ")
    score = float(input("Enter marks: "))
    marks[subject] = score   # Add subject and marks to dictionary

# Display the final dictionary
print("Marks Dictionary:")
print(marks)