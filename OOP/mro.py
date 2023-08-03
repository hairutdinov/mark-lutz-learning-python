class A:
    attr = 1
class B(A):
    pass
class C(A):
    attr = 2
class D(B, C):
    pass
    # attr = B.attr # эмуляция DFLR (depth first, left-to-right)

x = D()
print(x.attr) # для классов нового стиля посетит x, D, B, C (найдет attr) и только потом A
print(D.__mro__)
