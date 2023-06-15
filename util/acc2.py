import random


class StandardPolicy:

    @staticmethod
    def deposit(account, amount):
        account._balance += amount

    @staticmethod
    def withdraw(account, amount):
        if account._balance < amount:
            raise ValueError('Insufficient balance')
        account._balance -= amount

    @staticmethod
    def inquiry(account):
        return account._balance


class Account:
    num_accounts = 0

    def __init__(self, name, balance, policy=StandardPolicy):
        self.name = name
        self._balance = balance
        self.policy = policy
        Account.num_accounts += 1

    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext('name'), float(doc.findtext('balance')))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        if not 4 <= len(value) <= 10:
            raise ValueError('Name must be between 4 and 10 characters long')
        # if not value.isalnum():
        #     raise ValueError('Name must be alphanumeric')
        self._name = value

    def deposit(self, amount):
        self.policy.deposit(self, amount)

    def withdraw(self, amount):
        self.policy.withdraw(self, amount)

    def inquiry(self):
        return self.policy.inquiry(self)

    def __str__(self):
        return f'Account({self.policy} - {self.name}, {self._balance})'

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

nk = Account("Zenon", 1000)
nk.deposit(100)
print(nk)


# hp = Account("Zenon", 1000, HackPolicy)
# hp.deposit(100)
# print(hp)