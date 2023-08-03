class AccessControl:
    def __setattr__(self, key, value):
        if key == 'age':
            # self.__dict__[key] = value + 10
            # or
            object.__setattr__(self, key, value + 10)
        else:
            raise AttributeError(key + ' not allowed')

X = AccessControl()
X.age = 25
print(X.age)
X.name = 'Bob'