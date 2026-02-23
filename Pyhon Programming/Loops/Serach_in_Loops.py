num = (1, 2, 30, 40, 50, 60, 70, 80, 90, 100)

x = int(input("Enter a number: "))

i = 0
while i < len(num):
    if num[i] == x:
        print("Found!!")
        break
    i += 1
else:
    print("Not Found!")  
