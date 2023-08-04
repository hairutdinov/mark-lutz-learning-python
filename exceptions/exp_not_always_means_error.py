while True:
    try:
        str_number = input('Write some number and i\'ll tell you if it\'s even or odd: ')
        number = int(str_number)
    except (EOFError, SystemExit, KeyboardInterrupt):
        break
    except ValueError:
        print('Except number')
    else:
        print('even' if number % 2 == 0 else 'odd')
