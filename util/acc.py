
class Account:
    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext('name'), float(doc.findtext('balance')))

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


class HackAccount(Account):
    pass





a = Account('Guido', 1000)
b = Account('Bill', 10)
c = Account('Larry', 1000000)
c1 = HackAccount('Larry', 66660000)

data = '''
<account>
<name>Guido</name>
<balance>1000</balance>
</account>
'''

print(Account.num_accounts)
print(a.num_accounts)
print(c1)
c2 = HackAccount.from_xml(data)
print(c2)


d = Account.from_xml(data)
e = Account('Krzysztof', 2221000)
print(a)
print(b)
print(c)
print(d)
print(e)

