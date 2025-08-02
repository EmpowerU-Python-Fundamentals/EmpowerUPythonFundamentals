from classes.bank_account import BankAccount

def test_bank_account():
    # Test creating a BankAccount
    my_account = BankAccount("123456789", "John Doe", 1000.0)
    assert my_account.account_holder == "John Doe"
    try:
        _ = my_account.account_number
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass

    # Test checking the balance
    assert my_account.check_balance() == 1000.0

    # Test depositing money
    my_account.deposit(500.0)
    assert my_account.check_balance() == 1500.0

    # Test withdrawing money
    my_account.withdraw(250.0)
    assert my_account.check_balance() == 1250.0

    # Test withdrawing too much money
    my_account.withdraw(3000.0)
    assert my_account.check_balance() == 1250.0

    # Test setting account holder
    try:
        my_account.account_holder = "Jane Doe"
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass