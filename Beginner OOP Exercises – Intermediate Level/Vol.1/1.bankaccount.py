# Create a class BankAccount with the following:

# Attributes: account_holder, balance

# Method display_balance() – shows current balance

# Method deposit(amount) – adds to the balance

# Method withdraw(amount) – subtracts from the balance



# i'm importing the class named BankAccount from 4.bank_account.py that i made it in the folder 18.06.2025
class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name=holder_name
        self.balance=balance
    
    def display_balance(self):
        print(f"Mister {self.holder_name} has a balance {self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


john=BankAccount("John Wick", 125)
john.display_balance()
john.deposit(500000)
john.withdraw(250000)
john.display_balance()


