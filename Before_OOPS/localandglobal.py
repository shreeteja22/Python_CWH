x = "Walter white"
print(x)

def welcome():
    global x
    x = "Bryan Cranston"
    print("Heisenberg is", x)
    y = "Jesse pinkman"

welcome()
print(x)
#Local Variables
# Definition: A local variable is one that is defined within a function and is only accessible within that function.
# Global Variables
# Definition: A global variable is one that is defined outside of any function and is accessible throughout the program, including inside functions.