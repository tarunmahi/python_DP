"""
Encapsulation: Encapsulation is the process of bundling data (attributes) and methods that operate on that data into a single unit called a class. 
It provides data hiding and abstraction, allowing objects to interact with each other through well-defined interfaces.
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

account=BankAccount(123456,100)
account.deposit(500)
print(account.get_balance())