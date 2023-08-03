class Super():
    def hello(self):
        self.data1 = 'spam'


class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

x = Sub()
x.hello()
x.hola()
# x.data3 = 'toast'
x.__dict__['data3'] = 'ham'
print(x.__dict__)
print(x.__class__)
print(Sub.__bases__)
print(Super.__bases__)