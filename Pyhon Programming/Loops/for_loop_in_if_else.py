# Demonstrating for loop within if-else logic

# Sample data: List of numbers
numbers = [1, 2, 3, 4, 5]

# Check if the list is not empty
if numbers:
    print("The list contains the following numbers:")
    # Using a for loop to iterate through the list
    for number in numbers:
        print(number)
else:    
    print("The list is empty.")