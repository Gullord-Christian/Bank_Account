class BankAccount:
    def __init__(self, name, int_rate): 
        self.name = name
        self.int_rate = int_rate
        self.balance = 0

    def account (self, account):
        self.account = account
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print (f"Name: {self.name} - Balance is: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self


User1 = BankAccount("Chris", 0.05)
User2 = BankAccount("Taylor", 0.06)

User1.make_deposit(400).make_deposit(1000).yield_interest().display_account_info()

print("")

User2.make_deposit(500).make_deposit(1000).make_withdraw(2000).yield_interest().display_account_info()

#The class should also have the following methods:

# 1. deposit(self, amount) - increases the account balance by the given amount

# 2. withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5

# 3. display_account_info(self) - print to the console: eg. "Balance: $100"

# 4.  yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)