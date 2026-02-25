
# In this we will see how to read a file in python and print the content of the file on the console.
# To read a file in python we use the open() function. The open() function takes the name of the file as an argument and returns a file object.
# The file object has a method called read() which reads the content of the file and returns it as a string.
# Here is an example of how to read a file in python and print the content of the file on the console.

# Open the file in read mode
file = open("Demo.txt", "r") # The open() function takes two arguments: the name of the file and the mode in which we want to open the file. The mode can be "r" for read, "w" for write, "a" for append, and "x" for exclusive creation. In this case, we are opening the file in read mode, which means we can only read the content of the file and not modify it.
# Read the content of the file
content = file.read() # The read() method reads the entire content of the file and returns it as a string. If the file is large, it may take some time to read the entire content of the file. In such cases, we can use the readline() method to read the file line by line or the readlines() method to read all the lines of the file and return them as a list of strings.
# Print the content of the file
print(content)
# Close the file
file.close()    
