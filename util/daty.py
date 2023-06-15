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
