class limiter(object):
    __slots__ = ['age', 'name', 'job']

x = limiter()
x.age = 19
print(x.age)
# x.ape = 'spam'


class D:
    __slots__ = ['a', 'b']
    def __init__(self):
        self.d = 4
# i = D()


class Slotful:
    __slots__ = ['a', 'b', '__dict__']
    def __init__(self, data):
        self.c = data
I = Slotful(3)
I.a, I.b = 1, 2
print(I.a, I.b, I.c)
print(I.__dict__)
print([x for x in dir(I) if not x.startswith('__')])
print(getattr(I, 'a'), getattr(I, 'c'))
for a in (x for x in dir(I) if not x.startswith('__')):
    print(a, getattr(I, a))