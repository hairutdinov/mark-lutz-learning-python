class X:
    a = 1

I = X()
X.a = 2
J = X()
# print(I.a)
# print(X.a)
# print(J.a)


class C:
    # хранится в классе и разделяется
    shared = []
    def __init__(self):
        self.perobj = []

x = C()
y = C()
x.shared.append('spam')
x.perobj.append('spam')

print(y.shared, y.perobj)