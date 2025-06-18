# BankAccount class
# The class has account_holder_name and balance. Create a method display_balance() that shows the balance.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.balance=balance


account_status=BankAccount("John Smith", "125.850.742,25 EURO")

print(f"Mister {account_status.account_holder} has a balance of {account_status.balance}")