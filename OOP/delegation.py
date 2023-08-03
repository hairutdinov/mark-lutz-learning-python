class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, item):
        print('Trace: ', item)
        return getattr(self.wrapped, item)


if __name__ == '__main__':
    x = Wrapper([1, 2, 3])
    x.append(4)
    print(x.wrapped)

    y = Wrapper({'a': 1})
    print(y.keys())