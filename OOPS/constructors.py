class Person:
    def __init__(self,name , occupation):
        print("this function just get calls everytime whenever we use __init__ builtin")
        self.name = name
        self.occ = occupation

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Shreeram","Developer")
b = Person("Harry","Youtuber")
a.info()
b.info()