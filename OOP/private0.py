class PrivateException(Exception):
    pass

class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateException(key, self)
        else:
            self.__dict__[key] = value

class Test1(Privacy):
    privates = ['age']
class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

x = Test1()
# x.age = 25
x.name = 'Sam'
print(x.name)

y = Test2()
# y.name = 'John'
print(y.name)