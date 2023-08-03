try:
    raise IndexError('spam')
except IndexError:
    print('propagating')
    raise