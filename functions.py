# def func():
#     print("First function")
# func()
# other_func = func
# other_func()
# other_func.attr = 'value'
# print(other_func.attr)


# def times(x, y):
#     return x * y
# print(times(4, 2))
# print(times('Hi!', 4))


# def intersect(seq1, seq2):
#     return [x for x in seq1 if x in seq2]
# print(intersect([1,2], [3,4,5,2]))
# print(intersect('abc', 'cde'))


# import builtins
# print(dir(builtins))

# var = 98
# def global1():
#     import functions
#     functions.var += 1
# def global2():
#     import sys
#     glob = sys.modules['functions']
#     glob.var += 1
# global1()
# global2()
# print(var)



# x = 99
# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()
# f1()


# def f1():
#     X = 88
#     def f2():
#         print(X)
#     return f2
# action = f1()
# action()


# def maker(N):
#     def action(X):
#         return X ** N
#     return action
# square = maker(2)
# cub = maker(3)
# print(square(4))
# print(cub(4))


# def func(x):
#     return lambda n: x ** n
# print(func(4)(2))


# def makeActions():
#     return [lambda x, i=i: i ** x for i in range(5)]
#     # acts = []
#     # for i in range(5):
#     #     acts.append(lambda x: i ** x)
#     # return acts
# acts = makeActions()
# print(acts[0](1))
# print(acts[1](1))
# print(acts[3](2))


# def tester(start):
#     state = start
#     def nested(label):
#         nonlocal state
#         print(label, state)
#         state += 1
#     return nested
# F = tester(0)
# F('spam')
# G = tester(42)
# G('eggs')
# F('ham')


# def tester(start):
#     def nested(label):
#         print(label, nested.state)
#         nested.state += 1
#     nested.state = start
#     return nested
# F = tester(0)
# F('spam')
# G = tester(42)
# G('eggs')
# F('ham')


# from makeopen import makeopen
# makeopen('spam')
# F = open('testjson.json', 'r')
# print(F.read())


def echo(message):
    print(message)
# x = echo
# x('Hello')

# def inderect(func, arg):
#     func(arg)
# inderect(echo, 'Hello from inderect')


# schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
# for (func, arg) in schedule:
#     func(arg)


# def func(a):
#     b = 'spam'
#     return a * b
# print(func(8))
# print(func.__name__)
# print(func.__code__)
# print(func.__code__.co_argcount)
# print(func.__code__.co_varnames)
# func.count = 0
# func.count += 1
# print(func.count)
# print(dir(func)[-5:])


# def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
#     return a + b + c
# print(func())
# print(func.__annotations__)

