class A:
    pass

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()
print(type(a))
print(isinstance(a, A))
print(isinstance(b, A))
print(isinstance(b, B))
print(issubclass(B, A))
print(issubclass(C, A))