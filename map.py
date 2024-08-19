def cube(x):
    return x*x*x

print(cube(9))    ##The map() function in Python is used to apply a specified function to each item of an iterable (like a list) and returns a map object (which is an iterator) containing the results. It's useful when you want to transform or process elements of a collection without using a loop.

l = [1, 35, 353, 2, 4, 53, 3]

# Using the cube function with map
newl = list(map(cube, l))
print(newl)  # This will use the cube function you defined earlier.

# Using a lambda function with map to calculate the cube
newl_lambda = list(map(lambda x: x * x * x, l))
print(newl_lambda)  # This will give the same result using a lambda function.



#reduce func
from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)

