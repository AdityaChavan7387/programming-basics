# Here we will see how to use function types in Python

# A function that takes two integers and returns their sum
def add(a: int, b: int) -> int:
    return a + b    

# A function that takes a string and returns its length
def length(s: str) -> int:
    return len(s)   

# A function that takes a list of integers and returns their average
def average(nums: list[int]) -> float:
    return sum(nums) / len(nums) if nums else 0.0   

# A function that takes a function and a list of integers, and applies the function to each integer
def apply_function(func: callable, nums: list[int]) -> list: # type: ignore
    return [func(num) for num in nums]

# Example usage
if __name__ == "__main__":  
    print(add(3, 5))  # Output: 8
    print(length("Hello, World!"))  # Output: 13
    print(average([1, 2, 3, 4, 5]))  # Output: 3.0
    print(apply_function(lambda x: x * x, [1, 2, 3, 4]))  # Output: [1, 4, 9, 16]


