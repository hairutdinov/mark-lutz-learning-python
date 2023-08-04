# try:
#     try:
#         1 / 0
#     finally:
#         print('try/finally second level')
# finally:
#     print('try/finally first level')

def action2():
    return 1 + []
def action1():
    try:
        action2()
    except TypeError:
        print('inner try')
try:
    action1()
except TypeError:
    print('outer try')  # won't be printed
