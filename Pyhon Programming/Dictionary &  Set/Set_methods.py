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

# 5. update() method
# This method is used to update the set with the union of itself and another iterable (like list, set, etc.).
my_set.update([3, 4])
print(my_set)  # Output: {1, 2, 3, 4}

# 6. union() method
# This method is used to return a new set that is the union of the set and another set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}    
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5} 

# 7. intersection() method
# This method is used to return a new set that is the intersection of the set and another set.
intersection_set = set1.intersection(set2)  
print(intersection_set)  # Output: {3}
