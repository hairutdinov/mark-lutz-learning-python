# def changer(a, b):
#     a = 2
#     b[0] = 'spam'
# X = 1
# L = [1, 2]
# changer(X, L)
# print(X, L)


# def tester(start):
#     state = [start]
#     def nested(label):
#         print(label, state[0])
#         state[0] += 1
#     return nested
# F = tester(0)
# N = tester(5)
# F('spam')
# N('ham')
# N('toast')
# F('eggs')


# def func(a, *args):
#     print(a, args)
# func(1, 2, 3, 4)


# def f(**kwargs):
#     print(kwargs)
# f(a=1, b=2)


# def f(a, b):
#     print(f'a: {a}\nb: {b}')
# f(*[1, 2])


# if False:
#     action, args = lambda tpl: print(tpl), (1, )
# else:
#     action, args = lambda name, age: print(f'My name is {name} and i\'m {age} years old'), ['Bulat', 25]
# action(*args)


# def kwonly(a, *b, c):
#     print(a, b, c)
# kwonly(1, 2, c=3)
# kwonly(1, 2) # missing 1 required keyword-only argument: 'c'


# def kwonly(a, *, b, c):
#     print(a, b, c)
# takes 1 positional argument but 2 positional arguments (and 2 keyword-only arguments) were given
# kwonly(1, 2, b=1, c=2)


# def process(*args, notify=True):
#     print(args)
#     print(notify)
# process(1, 2, 3)


# def min1(*args):
#     min = args[0]
#     for arg in args[1:]:
#         if arg < min:
#             min = arg
#     return min
# def min2(first, *args):
#     for arg in args:
#         if arg < first:
#             first = arg
#     return first
# def min3(*args):
#     tmp = list(args)
#     tmp.sort()
#     return tmp[0]
# print(min1(1, 2, 3, -2, -1))
# print(min2('cc', 'bb', 'dd'))
# print(min3(-1, -2, -3, 1, 2, 3))


# def intersect(*args):
#     res = []
#     for first_seq_item in args[0]:
#         if first_seq_item in res:
#             continue
#         for other_seq in args[1:]:
#             if first_seq_item not in other_seq:
#                 break
#         else:
#             res.append(first_seq_item)
#     return res
# print(intersect((1, 2, 3, 4, 5), (3, 4, 5), (5, 1)))


# def union(*args):
#     res = []
#     for seq in args:
#         for x in seq:
#             if x not in res:
#                 res.append(x)
#     return res
# print(union('spam', 'ham'))
