import random


class StandardPolicy:

    @staticmethod
    def deposit(account, amount):
        account.balance += amount

    @staticmethod
    def withdraw(account, amount):
        if account.balance < amount:
            raise ValueError('Insufficient balance')
        account.balance -= amount

    @staticmethod
    def inquiry(account):
        return account.balance


class Account:
    num_accounts = 0

    def __init__(self, name, balance, policy=StandardPolicy):
        self.name = name
        self.balance = balance
        self.policy = policy
        Account.num_accounts += 1

    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext('name'), float(doc.findtext('balance')))

    def deposit(self, amount):
        self.policy.deposit(self, amount)

    def withdraw(self, amount):
        self.policy.withdraw(self, amount)

    def inquiry(self):
        return self.policy.inquiry(self)

    def __str__(self):
        return f'Account({self.policy} - {self.name}, {self.balance})'

    def __repr__(self):
        return str(self)


class HackPolicy(StandardPolicy):
    @staticmethod
    def deposit(account, amount):
        account.balance += 0.95 * amount

    @staticmethod
    def inquiry(account):
        if random.randint(0, 4) == 1:
            return 1.10 * account.balance
        else:
            return account.balance


data = '''
<account>
<name>Guido</name>
<balance>1000</balance>
</account>
'''

acc = Account.from_xml(data)
print(acc)

acc.deposit(100)
print(acc)

hp = Account("Zenon", 1000, HackPolicy)
hp.deposit(100)
print(hp)