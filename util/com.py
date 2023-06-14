import random

lista_1 = [11, 22, 33, 44, 55]

lista_x = ['Parzysta' if x % 2 == 0 else 'Nieparzysta' for x in lista_1]
print(lista_x)

lista = [x / 10 if x % 2 == 0 else 'Nieparzysta' for x in range(1, 30)]
print(lista)

numbers = {x // 2 for x in range(1, 30)}
print(numbers)

slownik = {x: x // 2 for x in range(1, 20)}
print(slownik)

kombo = {x ** 2: [y for y in range(x)] for x in range(5)}
print(kombo)

losowo = {x: random.randint(1, 100) for x in range(10)}
print(losowo)

losowo2 = [random.random() for _ in range(10)]
pow_50 = [x for x in losowo2 if x > 0.5]
print(losowo2)
print(pow_50)

kombo2 = [(x, y) for x in range(1, 10) for y in range(1, 10)]
print(kombo2)
kombo3 = [[x[0], x[1]] for x in kombo2]
print(kombo3)
