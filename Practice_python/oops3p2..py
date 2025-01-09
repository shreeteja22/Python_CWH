class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Should be positive")

    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance = 