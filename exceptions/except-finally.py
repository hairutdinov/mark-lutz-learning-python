def raise1(): raise IndexError
def noraise(): return
def raise2(): raise SyntaxError

for func in (raise1, noraise, raise2):
    print('<{}>'.format(func.__name__))
    try:
        try:
            func()
        except IndexError:
            print('Caught IndexError')
    finally:
        print('finally run')
    print('...')
