class BankAccount:
    #without encapsulation
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Should be positive")
    
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Invlaid")
        else:
            print("enter positive")

account = BankAccount(1000)
print(f"Initial Balance: {account.balance}")

account.deposit(500)
print(f"Balance after deposit: {account.balance}")

account.withdraw(300)
print(f"Balance after withdrawal: {account.balance}")

account.balance = -100 #this cant be modified
print(f"Balance after direct modification: {account.balance}")