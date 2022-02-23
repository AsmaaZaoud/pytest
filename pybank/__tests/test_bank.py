# test_bank.py

import pytest
from pybank.bank import Account, InsufficientAmount


@pytest.fixture
def linus_account():
    '''Returns an Account instance with customer name Linus and balance of zero'''
    return Account(name = "Linus")

@pytest.mark.parametrize("deposit,withdrawal,expected", [
    (2500, 800, 1700),
    (950, 75, 875),
])
def test_transactions(linus_account, deposit, withdrawal, expected):
    linus_account.deposit(deposit)
    linus_account.withdraw(withdrawal)
    assert linus_account.balance == expected
    
@pytest.fixture
def jack_account():
    '''Returns an Account instance with customer name Jack and a balance of zero'''
    return Account(name = "Jack")

@pytest.fixture
def jill_account():
    '''Returns an Account instance with customer name Jill and a balance of 250'''
    return Account(name = "Jill", balance = 250)

def test_setting_name(jack_account):
    assert jack_account.name == "Jack"
    
def test_default_balance(jack_account):
    assert jack_account.balance == 0   

def test_setting_balance(jill_account):
    assert jill_account.balance == 250

def test_account_deposit(jill_account):
    jill_account.deposit(120)
    assert jill_account.balance == 370

def test_account_withdraw(jill_account):
    jill_account.withdraw(10)
    assert jill_account.balance == 240

def test_account_withdraw_raises_exception_on_insufficient_amount(jack_account):
    with pytest.raises(InsufficientAmount):
        jack_account.withdraw(100)
