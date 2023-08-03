def gensquares(N):
    for i in range(N):
        yield i ** 2

# for i in gensquares(5):
#     print(i, end=' : ')

# print('\n' * 2, end='')

# x = gensquares(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


def ups(line):
    for sub in line.split(','):
        yield sub.upper()

# print(tuple(ups('aa,bb,cc')))
# print({i: s for (i, s) in enumerate(ups('aa,bb,cc'))})


# def gen():
#     for i in range(10):
#         X = yield i
#     print(X)
# G = gen()
# print(next(G))
# print(G.send(77))
# print(G.send(88))
# print(next(G))


# print(''.join(x.upper() for x in 'aa,bb,cc'.split(',')))
# a, b, c = (f'{x}\n' for x in 'aa,bb,cc'.split(','))
# print(a, end='')
# print(c, end='')


# G = (c * 4 for c in 'SPAM')
# I1 = iter(G)
# print(I1.__next__())
# print(next(I1))
# I2 = iter(G)
# print(next(I2))


# import os
# for (root, subs, files) in os.walk('.'):
#     for name in files:
#         if not any([root.startswith('./venv'), root.startswith('./.idea')]):
#             print(root, name)


def f(a, b, c):
    print('%s, %s and %s' % (a, b, c))

# f(*range(3))
# f(*(i for i in range(3)))
D = dict(a='Bob', b='dev', c=40.5)
# f(**D)
# f(*D)

L, S = [1, 2, 3], 'spam'
# for i in range(len(S)):
#     S = S[1:] + S[:1]
#     print(S, end=' ')
# for i in range(len(S)):
#     S = S[i:] + S[:i]
#     print(S, end=' ')


def scramble(seq):
    return (seq[i:] + seq[:i] for i in range(len(seq)))

# print(list(scramble('spam')))

import sys
sys.stdout = open('permute1.log', 'w')
def permute1(seq, tab: str = ''):
    print(tab + f'permute1({seq})')
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            print(f'{tab} i: {i}, rest: {rest}')
            for x in permute1(rest, tab+'\t'):
                print(f'{tab} cmd: res.append seq[i:i+1]: {seq[i:i+1]}, x: {x}')
                res.append(seq[i:i+1] + x)
            print()
        return res

print(permute1([1, 2, 3, 4]))
