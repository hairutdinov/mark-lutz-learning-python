class C2:
    pass


class C3:
    pass


class C1(C2, C3):
    def __init__(self):
        pass

    def set_name(self, who):
        self.name = who


I1 = C1()
I2 = C1()

I1.set_name('bob')
C1.set_name(I2, 'sue')

print(I1.name)
print(I2.name)
