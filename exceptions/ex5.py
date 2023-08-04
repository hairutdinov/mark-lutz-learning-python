class E(Exception): pass
try:
    raise E('spam')
except E as e:
    print(e)
    print(e.args)
    print(repr(e))