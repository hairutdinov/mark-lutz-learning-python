class ExitLoop(Exception): pass

try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise ExitLoop
                print('loop3: {}'.format(i))
            print('loop2')
        print('loop1')
except ExitLoop:
    print('continuing')