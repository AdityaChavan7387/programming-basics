# Search for a number x in this tuple using loop:

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 25
found = False
for element in list:
    if element == x:
        found = True
        break
if found:
    print(f"{x} is found in the list.")
else:    
    print(f"{x} is not found in the list.")
