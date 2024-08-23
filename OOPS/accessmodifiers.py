class employee:
    def __init__(self):
        self.__name = "Shreeram"

a = employee()
#print(a.__name)
#Cannot be accessed directly 
print(a._employee__name)
#Can be accessed indirectly
print(a.__dir__()) #it will give how many builtins are being acted in this code