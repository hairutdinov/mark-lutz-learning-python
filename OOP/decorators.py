class Spam:
    num_instances = 0
    def __init__(self):
        Spam.num_instances += 1
    @staticmethod
    def print_num_instances():
        print(f'Number of instances created: {Spam.num_instances}')

x, y = Spam(), Spam()
Spam.print_num_instances()


class properties(object):
    @property
    def age(self):
        return 25
i = properties()
print(i.age)

# ------------------------------------------------------

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)

# same as spam = tracer(spam)
@tracer
def spam(a, b, c):
    return a + b + c

print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))

# ------------------------------------------------------

def tracer(func):
    calls = 0
    def oncall(*args):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args)
    return oncall

class C:
    @tracer
    def spam(self, a, b, c):
        return a + b + c
x = C()
print(x.spam(1, 2, 3))
