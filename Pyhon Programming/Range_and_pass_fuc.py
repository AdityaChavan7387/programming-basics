# In this we will see how the range and pass function works in python   

# Range function is used to generate a sequence of numbers, which can be used in for loops or other contexts where you need a sequence of numbers.
# The syntax of the range function is as follows:
# range(start, stop, step)
# - start: The starting point of the sequence (inclusive). Default is 0.
# - stop: The end point of the sequence (exclusive).
# - step: The increment between each number in the sequence. Default is 1.
# Example of using range function
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
# Example of using range function with start and stop
for i in range(2, 10):
    print(i)
# Output: 2, 3, 4, 5, 6,
# 7, 8, 9
# Example of using range function with start, stop and step
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
# The pass statement is a null statement in Python. It is used as a placeholder when you need to write code but don't want to execute anything.
# The syntax of the pass statement is as follows:
# pass
# Example of using pass statement
def my_function():
    pass
# In this example, the my_function is defined but it does not do anything because of the
# pass statement. You can use the pass statement in loops, functions, or any other block of code where you need to write code but don't want to execute anything.
# Example of using pass statement in a loop
for i in range(5):
    if i % 2 == 0:
        pass  # This will do nothing for even numbers
    else:
        print(i)  # This will print odd numbers
# Output: 1, 3
