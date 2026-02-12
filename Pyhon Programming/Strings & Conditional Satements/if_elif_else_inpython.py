Age = int(input("Enter your age: ")) #input() function is used to take input from the user. It takes a string as an argument and returns a string. In this case, we are taking the age as input from the user and converting it to an integer using the int() function.

if (Age >= 18):    #if statement checks if the condition is true or false. If the condition is true, it executes the block of code inside the if statement. If the condition is false, it skips the block of code and moves to the next statement.
    print("You are an adult") 

elif (Age >= 13 and Age < 18): #elif statement is used to check multiple conditions. It is used after an if statement and before an else statement. It allows you to check for multiple conditions and execute different blocks of code based on the condition that is true.
    print("You are a teenager") 
else:        #else statement is used to execute a block of code if the condition in the if statement is false. It is used after an if statement and after any number of elif statements. It is executed when all the conditions in the if and elif statements are false.
    print("You are a child")