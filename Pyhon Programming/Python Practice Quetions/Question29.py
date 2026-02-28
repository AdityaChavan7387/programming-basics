# Create Account Class with 2 attributes: account number and balance
#Create methods for debit,credit and printing the balance
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Rs.", amount, "debited from account")
            print("Current balance: Rs.", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "credited to account")
        print("Current balance: Rs.", self.balance)

    def print_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

# Create an instance of the Account class
account = Account("123456789", 1000)
# Test the methods
account.print_balance()  # Output: Account Number: 123456789, Balance: 1000
account.debit(200)
account.print_balance()  # Output: Account Number: 123456789, Balance: 800
account.credit(500)
account.print_balance()  # Output: Account Number: 123456789, Balance: 1300

