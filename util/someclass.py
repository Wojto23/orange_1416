class SomeClass:
    @property
    def attr(self):
        print('attr getter')

    @attr.setter
    def attr(self, value):
        print('attr setter', value)

    @attr.deleter
    def attr(self):
        print('attr deleter')


s = SomeClass()
s.attr
s.attr = 1
del s.attr


class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


b = Box(4, 5)
print(b.area)
print(b.perimeter)
# b.area = 10 # AttributeError: can't set attribute

class SomeClass:
    def hej(self):
        print('hej')

c = SomeClass()
c.hej()
