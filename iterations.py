# f = open('script2.py')
# while True:
#     try:
#         print(f.__next__(), end='')
#     except StopIteration:
#         break
# f.close()
# print('file closed')

# лучший способ чтения файла строка за строкой - не читать его вообще,
# а взамен позволить циклу for автоматически вызывать метод __next__ на каждой итерации
# for line in open('script2.py'):
#     print(line.upper(), end='')

# L = [1, 2, 3]
# I = iter(L)
# print(I.__next__())
# print(next(I))
# print(next(I))

# print([(offset, line.rstrip()) for (offset, line) in enumerate(open('script2.py'))])

# print([(offset, line.rstrip()) for (offset, line) in enumerate(open('script2.py')) if line[:5] == 'print'])

# print([x + y for x in 'abc' for y in 'xyz'])

# from functools import reduce
# from operator import mul
# print(reduce(mul, [1, 2, 3]))


