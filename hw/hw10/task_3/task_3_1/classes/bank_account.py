class BankAccount:
    _account_number: str
    _account_holder: str
    _balance: float
    
    def __init__(self, an, ah, b):
        self._account_number = an
        self._account_holder = ah
        self._balance = b

    @property
    def account_holder(self):
        return self._account_holder
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance = self._balance - amount
        else:
            print(f"Insufficient funds")
            
    def check_balance(self):
        return self._balance