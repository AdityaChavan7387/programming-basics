
# Write A program to check if a number is multiple of 7 or not.

number = int(input("Enter a number: ")) # The input function takes user input as a string, so we need to convert it to an integer for numerical comparison.

if (number % 7 == 0): # The if statement checks if the number is divisible by 7 without leaving a remainder. If this condition is true, it means the number is a multiple of 7.
    print(f"{number} is a multiple of 7.")
else:   
    print(f"{number} is not a multiple of 7.")

