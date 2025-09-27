import unittest
from bankAccount import BankAccount 

class TestBankAccount(unittest.TestCase): 
    """ 
    Unit testing of the class BankAccount
    """
    def setUp(self): 
        self.account = BankAccount()

    def test_initial_balance(self): 
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit_positive_amount(self): 
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 50)

    def test_deposit_negative_amount(self): 
        with self.assertRaises(ValueError): 
            self.account.deposit(-50)

    def test_withdraw_with_sufficient_funds(self): 
        self.account.deposit(50) 
        self.account.withdraw(30) 
        self.assertEqual(self.account.get_balance(), 20) 

    def test_withdraw_with_insufficient_funds(self): 
        self.account.deposit(50)
        with self.assertRaises(ValueError): 
            self.account.withdraw(100)

    def test_withdraw_negative_amount(self): 
        with self.assertRaises(ValueError):
            self.account.withdraw(-50) 