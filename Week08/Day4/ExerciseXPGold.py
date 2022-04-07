"""
Create a class called BankAccount that contains the following attributes and methods:
deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive
"""


class BankAccount:
    def __init__(self, username, password):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, number: int):
        if self.authenticated:
            if number > 0:
                self.balance += number
            else:
                raise ValueError("Number is not positive.")
        else:
            raise Exception("Authentication failed")

    def withdraw(self, number: int):
        if self.authenticated:
            if number > 0:
                self.balance -= number
            else:
                raise ValueError("Number is not positive.")
        else:
            raise Exception("Authentication failed")

    def authenticate(self, username, password):
        self.authenticated = self.username == username and self.password == password
        return self.authenticated


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.minimum_balance = 0

    def withdraw(self, number: int):
        if self.authenticated:
            if self.balance - number > self.minimum_balance:
                super().withdraw(number)
            else:
                raise Exception("Not enough funds.")
        else:
            raise Exception("Authentication failed")


class ATM:
    def __init__(self, account_list, try_limit):
        for acc in account_list:
            if not isinstance(acc, (BankAccount, MinimumBalanceAccount)):
                raise Exception("Bank accounts fail")
        self.account_list = account_list
        try:
            assert try_limit > 0
        except AssertionError:
            print("Attention!. try_limit is not positive!")
            self.try_limit = 2
        else:
            self.try_limit = try_limit
        self.current_tries = 0

    def show_main_menu(self):
        while True:
            username = input("Enter your username to log in, or input 'exit': ")
            if username == "exit":
                break
            password = input("Enter your password to log in, or input 'exit': ")
            if password == "exit":
                break
            if not self.log_in(username, password):
                print("Authentication failed")
                self.current_tries += 1
            if self.current_tries >= self.try_limit:
                print("Limit of tries has been reached. Bye-bye")
                break

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                self.show_account_menu(account)
                return True
        return False

    def show_account_menu(self, account):
        word = ""
        print(f"Welcome back, {account.username}.")
        while word != 'exit':
            word = input("What do you want do do (deposit, withdraw, exit)?\n")
            if word == "deposit":
                account.deposit(int(input("Enter a amount of funds to deposit: ")))
                print("Operation approved")
            elif word == "withdraw":
                account.withdraw(int(input("Enter a amount of funds to withdraw: ")))
                print("Operation approved")
        print(f"Bye-bye, {account.username}.")


caspee = ATM([BankAccount('gleb', 'gleb'), MinimumBalanceAccount('bennet', 'bennet')], 3)
caspee.show_main_menu()
