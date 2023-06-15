class Account:
    num_accounts = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError('Insufficient balance')
        self.balance -= amount

    def __str__(self):
        return f'Account({self.name}, {self.balance})'

    def __repr__(self):
        return str(self)