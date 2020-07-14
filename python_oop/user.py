class User:
    def __init__(self, username, email, cash=0):
        self.name = username
        self.email = email
        self.account_balance = cash
    def make_deposit(self, amt):
        self.account_balance += amt
    def make_withdrawal(self, amt):
        self.account_balance -= amt
    def display_user_balance(self):
        print(f"{self.name}, your current balance is ${self.account_balance}")
    def transfer_money(self, other_acct, amt):
        self.account_balance -= amt
        other_acct.account_balance += amt
        print(f"{self.name}, your transfer of ${amt} to {other_acct.name} has been completed. Your new account balance is ${self.account_balance}.\nBecause we don't believe in privacy, here's {other_acct.name}'s new account balance: ${other_acct.account_balance}.")

dan = User("Dan", "dan@rocketmail.com")
bob = User("Bob", "bob@gmail.com", 400)
karen = User("Karen", "karen@hotmail.com", 200)

dan.make_deposit(352)
dan.make_deposit(490)
dan.make_deposit(16)
dan.make_withdrawal(375)
dan.display_user_balance()

bob.make_deposit(1600)
bob.make_deposit(360)
bob.make_withdrawal(40)
bob.make_withdrawal(26)
bob.display_user_balance()

karen.make_deposit(1000)
karen.make_withdrawal(360)
karen.make_withdrawal(400)
karen.make_withdrawal(250)
karen.display_user_balance()

dan.transfer_money(karen, 10)