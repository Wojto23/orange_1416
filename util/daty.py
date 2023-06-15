import time

class Date:
    datefmt = '{year}-{month:02d}-{day:02d}'

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    def __str__(self):
        return self.datefmt.format(year=self.year, month=self.month, day=self.day)

    @classmethod
    def from_timestamp(cls, ts):
        tm = time.localtime(ts)
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

    @classmethod
    def today(cls):
        return cls.from_timestamp(time.time())

class EuroDate(Date):
    datefmt = '{day:02d}.{month:02d}.{year}'

class USDate(Date):
    datefmt = '{month:02d}/{day:02d}/{year}'

d = Date(2012, 12, 21)
d1 = Date.today()
print(d1)
print(d)
e = EuroDate(2012, 12, 21)
e1 = EuroDate.today()
print(e)
print(e1)
u = USDate(2012, 12, 21)
u1 = USDate.today()
print(u)
print(u1)

print(USDate.mro())