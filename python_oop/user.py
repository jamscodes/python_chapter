class User:
    def __init__(self, username, email, cash=0):
        self.name = username
        self.email = email
        self.account_balance = cash
    def make_deposit(self, amt):
        self.account_balance += amt
        return self
    def make_withdrawal(self, amt):
        self.account_balance -= amt
        return self
    def display_user_balance(self):
        print(f"{self.name}, your current balance is ${self.account_balance}")
        return self
    def transfer_money(self, other_acct, amt):
        self.account_balance -= amt
        other_acct.account_balance += amt
        print(f"{self.name}, your transfer of ${amt} to {other_acct.name} has been completed. Your new account balance is ${self.account_balance}.\nBecause we don't believe in privacy, here's {other_acct.name}'s new account balance: ${other_acct.account_balance}.")
        return self

dan = User("Dan", "dan@rocketmail.com")
bob = User("Bob", "bob@gmail.com", 400)
karen = User("Karen", "karen@hotmail.com", 200)

dan.make_deposit(352).make_deposit(490).make_deposit(16).make_withdrawal(375).display_user_balance()

bob.make_deposit(1600).make_deposit(360).make_withdrawal(40).make_withdrawal(26).display_user_balance()

karen.make_deposit(1000).make_withdrawal(360).make_withdrawal(400).make_withdrawal(250).display_user_balance()

dan.transfer_money(karen, 10)