class BankAccount: 
    """
    A class to represent a simple bank account in order to practice unit-testing.
    """
    def __init__(self, balance = 0): 
        self.balance = balance

    def deposit(self, amount): 
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount): 
        if amount <= 0: 
            raise ValueError(f"Deposit amount must be positive")
        if self.balance - amount < 0: 
            raise ValueError(f"Insufficient funds. Your current balance is: {self.balance}")
        self.balance -= amount
        
    def get_balance(self): 
        return self.balance 
