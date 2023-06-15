class A:
    def __init__(self):
        self.__x = 3

    def __spam(self):
        print('A.__spam', self.__x)

    def bar(self):
        self.__spam()

class B(A):
    def __init__(self):
        A.__init__(self)
        self.__x = 37

    def __spam(self):
        print('B.__spam', self.__x)

    def foo(self):
        self.__spam()


b = B()
b.bar()
b.foo()
print(vars(b))
b._A__spam()
b._B__spam()