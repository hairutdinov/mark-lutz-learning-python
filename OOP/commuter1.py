class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    # def __radd__(self, other):
    #     print('add', other, self.val)
    #     return other + self.val

    # OR
    # def __radd__(self, other):
    #     return self + other # поменять местами и снова сложить

    # OR
    __radd__ = __add__

x = Commuter1(5)
y = Commuter1(6)
print(x + 1)
print(x + y)