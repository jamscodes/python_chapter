from bank_account import BankAccount

class User:
    def __init__(self, username, email, cash=0):
        self.name = username
        self.email = email
        self.accounts = {
            'init_acct': BankAccount(cash, 0.02)
        }
    def make_deposit(self, amt, acct):
        self.accounts[acct].balance += amt
        return self
    def make_withdrawal(self, amt, acct):
        self.accounts[acct].balance -= amt
        return self
    def display_user_balance(self, acct='All'):
        if acct == 'All':
            for a in self.accounts:
                print(f"{self.name}, the current balance in your {a} account is ${self.accounts[a].balance}")
        else:
            print(f"{self.name}, the current balance in your {acct} account is ${self.accounts[acct].balance}")
        return self
    def transfer_money(self, acct, rec_user, other_acct, amt):
        self.accounts[acct].balance -= amt
        rec_user.accounts[other_acct].balance += amt
        print(f"{self.name}, your transfer of ${amt} from your {acct} account to {rec_user.name}'s {other_acct} has been completed.")
        self.display_user_balance(acct)
        return self
    def add_account(self, name, cash=0, int_rate=0.01):
        self.accounts[name] = (BankAccount(cash, int_rate))
        return self

jonathan = User("Jonathan", "jonathan@email.com", 400)
joshua = User("Joshua", "joshua@email.com", 400)

jonathan.make_deposit(200,'init_acct').display_user_balance('init_acct').transfer_money('init_acct', joshua, 'init_acct', 100)

joshua.add_account('Savings').transfer_money('init_acct', joshua, 'Savings', 100).display_user_balance()