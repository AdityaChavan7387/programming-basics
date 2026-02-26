# Here we will see the different modes in which we can open a file in python. The open() function takes two arguments: the name of the file and the mode in which we want to open the file. The mode can be "r" for read, "w" for write, "a" for append, and "x" for exclusive creation. We can also use "b" for binary mode and "t" for text mode. By default, the mode is "r" for read and "t" for text.

# Open the file in write mode
file = open("Demo.txt", "w") # When we open a file in write mode, it will create a new file if the file does not exist. If the file already exists, it will overwrite the existing content of the file. So, be careful while opening a file in write mode as it can lead to data loss if you are not careful.
# Write some content to the file
file.write("This is a demo file for write mode.\n") # The write() method is used to write content to the file. It takes a string as an argument and writes it to the file. We can also use the writelines() method to write a list of strings to the file.
file.write("This is the second line of the demo file.\n")
# Close the file
file.close()    

# Open the file in append mode
file = open("Demo.txt", "a") # When we open a file in append mode, it will create a new file if the file does not exist. If the file already exists, it will append the new content to the existing content of the file. So, be careful while opening a file in append mode as it can lead to data duplication if you are not careful.
# Write some content to the file
file.write("This is a demo file for append mode.\n")
file.write("This is the second line of the demo file.\n")   
# Close the file
file.close()

# Open the file in exclusive creation mode
file = open("Demo.txt", "x") # When we open a file in exclusive creation mode, it will create a new file if the file does not exist. If the file already exists, it will raise a FileExistsError. So, be careful while opening a file in exclusive creation mode as it can lead to errors if you are not careful.
# Write some content to the file
file.write("This is a demo file for exclusive creation mode.\n")
file.write("This is the second line of the demo file.\n")
# Close the file
file.close()    

# Open the file in binary mode
file = open("Demo.txt", "rb") # When we open a file in binary mode, it will read the content of the file as bytes. This is useful when we are working with non-text files such as images, videos, etc. We can also use the write() method to write bytes to the file. In such cases, we need to encode the string to bytes before writing it to the file.
# Read the content of the file
content = file.read() # The read() method reads the entire content of the file and returns it as bytes. We can decode the bytes to a string using the decode() method.
# Print the content of the file
print(content.decode()) # The decode() method is used to decode the bytes to a string. We need to specify the encoding format while decoding the bytes. By default, the encoding format is "utf-8".
# Close the file
file.close()

# Open a Disk file for updating
file = open("Demo.txt", "+") # When we open a file in update mode, it allows us to read and write to the file. If the file does not exist, it will create a new file. If the file already exists, it will allow us to read and write to the existing content of the file. So, be careful while opening a file in update mode as it can lead to data loss if you are not careful.
# Read the content of the file
content = file.read()
print(content)
# Write some content to the file
file.write("This is a demo file for update mode.\n")
# Close the file
file.close()

# r+ mode is used to open a file for both reading and writing. The file pointer is placed at the beginning of the file. If the file does not exist, it will raise a FileNotFoundError.
file = open("Demo.txt", "r+")
# Read the content of the file
content = file.read()
print(content)
# Write some content to the file
file.write("This is a demo file for r+ mode.\n")
# Close the file
file.close()    

# w+ mode is used to open a file for both writing and reading. The file pointer is placed at the beginning of the file. If the file does not exist, it will create a new file. If the file already exists, it will overwrite the existing content of the file.
file = open("Demo.txt", "w+")
# Write some content to the file    
file.write("This is a demo file for w+ mode.\n")
# Read the content of the file
file.seek(0) # The seek() method is used to change the file pointer position. In this case, we are moving the file pointer to the beginning of the file so that we can read the content of the file after writing to it.
content = file.read()
print(content)
# Close the file
file.close()    