# Here we will see how to use Recursion in Python. Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.

# Let's start with a simple example of a recursive function that calculates the factorial of a number:
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1) 
    
# Now we can test the function:
print(factorial(5))  # Output: 120  
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1

# Another example of recursion is the Fibonacci sequence, where each number is the sum of the two preceding ones:
def fibonacci(n):   
    # Base case: if n is 0, return 0; if n is 1, return 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)