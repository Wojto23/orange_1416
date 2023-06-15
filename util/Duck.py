class Duck:
    def walk(self):
        return "Duck walk"

    def noise(self):
        return "Kwa Kwa"


class Dog:
    def noise(self):
        return "Hau Hau"

    def march(self):
        return "Dog march"


class Cat(Duck, Dog):
    pass


class Cyclist:
    def noise(self):
        return "Ding Ding"

    def pedal(self):
        return "Cyclist pedal"


# class NoiseMixin:
#     def noise(self):
#         raise NotImplementedError("Subclass must implement noise method")


class LoudMixin():
    def noise(self):
        return super().noise().upper()


class AnnoyingMixin():
    def noise(self):
        return 3 * super().noise()


class LoudDuck(LoudMixin, Duck):
    pass


class AnnoyingDog(AnnoyingMixin, Dog):
    pass


class LoudCyclist(LoudMixin, Cyclist):
    pass


d = LoudDuck()
print(d.noise())
g = AnnoyingDog()
print(g.noise())
c = LoudCyclist()
print(c.noise())
print(LoudCyclist.__mro__)
print(AnnoyingDog.__mro__)
