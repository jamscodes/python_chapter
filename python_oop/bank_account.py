class BankAccount:
    def __init__(self, balance=0, int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amt):
        self.balance += amt
        print(f"Your deposit of ${amt} has been completed. Your new balance is: ${self.balance}")
        return self
    def withdraw(self, amt):
        self.balance -= amt
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        print(f"Your withdrawal of ${amt} has been completed. Your new account balance is: ${self.balance}.")
        return self
    def display_account_info(self):
        print(f"Your current balance is: ${self.balance}.")
        return self
    def yield_interest(self):
        if self.balance > 0:
            yield_amt = self.balance * self.int_rate
            print(f"Your account has accrued ${yield_amt} in interest!")
            self.deposit(yield_amt)
        else:
            print(f"Your account is overdrawn and cannot accrue interest.")
        return self

Jonathan = BankAccount(400)

Jonathan.deposit(250).deposit(250).deposit(250).withdraw(150).yield_interest().display_account_info()

Andrew = BankAccount(0,0.05)

Andrew.deposit(250).deposit(250).withdraw(150).withdraw(150).withdraw(150).withdraw(150).yield_interest().display_account_info()