class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    @property
    def account_holder(self):
        return self._account_holder

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f'Your account has been replenished. Current balance: {self.__balance}'

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f'Withdrawal for the amount: {self.__balance}'
        else:
            return 'Insufficient funds'

    def check_balance(self):
        return self.__balance
