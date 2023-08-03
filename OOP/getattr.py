class Empty:
    def __getattr__(self, item):
        if item == 'age':
            return 25
        else:
            raise AttributeError(item)

X = Empty()
print(X.age)
print(X.name)

