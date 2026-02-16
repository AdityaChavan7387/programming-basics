
marks = [90, 80, 70, 60, 50]

# Slicing the list to get the first three marks
print(marks[0:3])

print(marks[:3])  # This is equivalent to marks[0:3]
print(marks[1:])  # This will give us all marks starting from index 1 to the end of the list

# now for negative indexing
print(marks[-3:])  # This will give us the last three marks
print(marks[:-2])  # This will give us all marks except the last two