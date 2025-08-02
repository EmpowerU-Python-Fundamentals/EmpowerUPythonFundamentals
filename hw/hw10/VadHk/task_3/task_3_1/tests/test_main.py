from classes.bank_account import BankAccount

def test_main():
    my_account = BankAccount("123456789", "John Doe", 1000.0)
    print(my_account.account_holder)

    try:
        _ = my_account.account_number
        print("Should have raised AttributeError")
    except AttributeError:
        print("AttributeError raised as expected")

    try:
        _ = my_account.balance
        print("Should have raised AttributeError")
    except AttributeError:
        print("AttributeError raised as expected")

    print(my_account.check_balance())

    my_account.deposit(500.0)
    print(my_account.check_balance())

    my_account.withdraw(250.0)
    print(my_account.check_balance())

    try:
        my_account.account_holder = "Jane Doe"
        print("Should have raised AttributeError")
    except AttributeError:
        print("AttributeError raised as expected")

    my_account.withdraw(5000.0)