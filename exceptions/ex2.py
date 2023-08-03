class Career(Exception):
    def __str__(self):
        return 'So i became a waiter...'

# raise Career()


def after():
    D = [1, 2, 3]
    try:
        print(D[3])
    finally:
        print('after indexing')
    print('after try?')
# after()

excp = None
try:
    1 / 0
except Exception as X:
    print(X)
    excp = X
print(excp.__repr__())
