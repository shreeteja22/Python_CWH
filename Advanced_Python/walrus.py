# The walrus operator (:=) was introduced in Python 3.8
# It is called the assignment expression or walrus operator.
# It allows you to assign values to variables as part of a larger expression.

# Example without the walrus operator:
# happy = False  
# print(happy)    

# Example with the walrus operator:
# The variable 'happy' is assigned the value True and printed in the same line
# print(happy := True)

# Another example without the walrus operator:
# foods = list()  # Initialize an empty list
# while True:
#   food = input("What food do you like?: ")  # Get user input
#   if food == "quit":   # Break the loop if the user enters "quit"
#       break
#   foods.append(food)   # Add the food to the list

# The same example with the walrus operator:

# Initialize an empty list to store foods
foods = list()

# Using the walrus operator to assign the input value to 'food' and check the condition in a single step
while (food := input("What food do you like?: ")) != "quit":
    # Append the food to the list until the user types "quit"
    foods.append(food)

# Explanation:
# (food := input("What food do you like?: ")) assigns the user input to the variable 'food'
# and checks if it's not equal to "quit" in the same line.
# This avoids writing the input statement twice (before and inside the loop).
