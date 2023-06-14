import itertools
import operator


def dodaj(a, b):
    return a + b


d = lambda a, b: a + b
print(d(2, 3))

values = dict(one=1, two=2, three=3)
print(values)
print(sorted(values.items(), key=lambda item: item[1]))
pobierz_wartosc = operator.itemgetter(1)
print(sorted(values.items(), key=pobierz_wartosc))

print(operator.concat("2", "3"))

months = [10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]
aku = list(itertools.accumulate(months, operator.add))
print(aku)

a = range(3)
b = range(5)
print(a)
print(b)
print(list(itertools.chain(a, b)))

iter = [range(3), range(5)]
print(list(itertools.chain.from_iterable(iter)))
print(list(itertools.compress(range(1000), [1, 0, 1, 0, 1, 1])))
print(list(itertools.dropwhile(lambda x: x < 3, range(10))))
print(list(itertools.takewhile(lambda x: x < 3, range(10))))

print(list(itertools.islice(itertools.count(), 10)))
print(list(itertools.islice(itertools.count(), 5, 10, 2)))
print(list(itertools.islice(itertools.count(10, 2.5), 5)))


def test(n):
    i = 1
    while i < n:
        yield i
        i += 1

def test2(n):
    i = 1
    while i < n:
        i += 1
        return i


gen = test(5)
ret = test(5)
print(ret)

for n in test(5):
    print(n)

# for n in test2(5):
#     print(n)


# print(next(gen))
# print("Tutaj to jest coś innego...")
# print(next(gen))
# print(next(gen))
# print(next(gen))


sekwencja = map(lambda x: x * 2, itertools.count())
# print(next(sekwencja))
# print(next(sekwencja))
# print(next(sekwencja))