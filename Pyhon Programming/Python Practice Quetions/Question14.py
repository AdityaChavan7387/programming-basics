# WAP to check if a list contains a palindrome of elements .(Hint: A palindrome is a sequence that reads the same backward as forward And Use Copy() method.)

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("List 1 is a palindrome.")
else:    
    print("List 1 is not a palindrome.")


