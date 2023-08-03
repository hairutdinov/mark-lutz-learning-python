class AgeDesc(object):
    def __get__(self, instance, owner):
        return 25
    def __set__(self, instance, value):
        instance._age = value


class descriptors(object):
    age = AgeDesc()

x = descriptors()
print(x.age)
x.age = 26
print(x._age)