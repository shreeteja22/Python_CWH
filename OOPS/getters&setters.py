class MyClass:
    # Constructor to initialize the value
    def __init__(self, value):
        self._value = value  # Initialize the private attribute _value
    
    # Method to display the current value
    def show(self):
        print(f"Value is {self._value}")  # Display the value of _value
    
    # Getter method for ten_value (decorated with @property)
    @property
    def ten_value(self):
        return 10 * self._value  # Return _value multiplied by 10

    
    # Setter method for ten_value (decorated with @ten_value.setter)
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10  # Update _value with the new value divided by 10


# Creating an instance of MyClass with an initial value of 10
obj = MyClass(10)

# Setting the ten_value using the setter (this will update _value)
obj.ten_value = 67

# Printing the ten_value using the getter (this will return _value * 10)
print(obj.ten_value)  # Output: 67.0

# Showing the current _value after setting ten_value to 67
obj.show()  # Output: Value is 6.7






#Getter and Setter Explained:
# Getter (@property): The ten_value property allows you to access _value in a modified form (10 times _value). The getter method is triggered when you try to read the ten_value property.
# Setter (@ten_value.setter): The setter allows you to change the _value attribute indirectly by setting ten_value. When you assign a value to ten_value, the setter method is called, updating _value to be one-tenth of the new value.





# Explanation:
# - The class `MyClass` has a private attribute `_value` which is initialized via the constructor.
# - The `show` method displays the current value of `_value`.
# - The `ten_value` property is a getter that returns `_value` multiplied by 10. 
# - The `ten_value` setter allows updating `_value` by setting a new value to `ten_value`. 
#   When you set `ten_value`, the setter takes the new value and divides it by 10 to update `_value`.
# - For example, when `obj.ten_value = 67` is called, the setter updates `_value` to `67 / 10 = 6.7`.
# - Consequently, when you print `obj.ten_value`, it returns `6.7 * 10 = 67.0`, and the `show` method 
#   displays the updated `_value` as 6.7.