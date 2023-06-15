class Account:
    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

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


a = Account('Guido', 1000)
b = Account('Bill', 10)
c = Account('Larry', 1000000)

print(Account.num_accounts)
print(a.num_accounts)

data = '''
<account>
<name>Guido</name>
<balance>1000</balance>
</account>
'''

