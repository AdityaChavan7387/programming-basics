
# Write A Program to find the greatest of three numbers entered by user.

num1 = float(input("Enter first number: ")) # The input function takes user input as a string, so we need to convert it to a float for numerical comparison.
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3): # The if statement checks if num1 is greater than or equal to both num2 and num3. If this condition is true, it means num1 is the greatest number among the three.
    print("The Greatest Number is From num1: ", num1)
elif (num2 >= num1) and (num2 >= num3):
    print("The Greatest Number is From num2: ", num2)
else:    
    print("The Greatest Number is From num3: ", num3)