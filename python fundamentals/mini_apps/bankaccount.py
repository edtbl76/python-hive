class BankAccount(object):
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)

    def show_balance(self):
        print("Balance: $%.2f" % (self.balance))

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount.")
            return
        else:
            print("Deposit Amount: $%.2f" % (amount))
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money in account.")
            return
        else:
            print("Withdrawing : $%.2f" % (amount))
            self.balance -= amount
            self.show_balance()


my_account = BankAccount("Ed")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)


# Ed's account. Balance: $0.00
# Balance: $0.00
# Deposit Amount: $2000.00
# Balance: $2000.00
# Withdrawing : $1000.00
# Balance: $1000.00
# Ed's account. Balance: $1000.00