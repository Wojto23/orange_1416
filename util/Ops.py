class Ops:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y


a = Ops.add(10, 20)
b = Ops.sub(10, 20)
c = Ops.mul(10, 20)
print(a, b, c)