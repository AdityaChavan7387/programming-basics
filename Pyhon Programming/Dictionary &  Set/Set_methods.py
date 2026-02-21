# Here we will see some of the methods of set

# 1. add() method
# This method is used to add an element to the set. If the element is already present in the set, it will not be added again.   
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)  # This will not be added again
print(my_set)  # Output: {1, 2}

# 2. remove() method
# This method is used to remove an element from the set. If the element is not present in the set, it will raise a KeyError.
my_set.remove(1)
print(my_set)  # Output: {2}    

# 3. clear() method
# This method is used to remove all elements from the set.
my_set.add(1)
my_set.add(2)
print(my_set)  # Output: {1, 2}
my_set.clear()
print(my_set)  # Output: set()

# 4. pop() method
# This method is used to remove and return an arbitrary element from the set. If the set is empty, it will raise a KeyError.
my_set.add(1)
my_set.add(2)
print(my_set)  # Output: {1, 2}
element = my_set.pop()
print(element)  # Output: 1 or 2 (arbitrary element)
print(my_set)  # Output: {2} or {1} (remaining element) 

