class Spam:
    num_instances = 0
    def __init__(self):
        Spam.num_instances += 1
    def print_num_instances(cls):
        print(f'Number of instances created: {cls.num_instances} {cls}')
    print_num_instances = classmethod(print_num_instances)


class Sub(Spam):
    def print_num_instances(cls):
        print('Extra stuff..', cls)
        Spam.print_num_instances()
    print_num_instances = classmethod(print_num_instances)


class Other(Spam): pass

# a, b = Spam(), Spam()
# a.print_num_instances()
# Spam.print_num_instances()

x = Sub()
y = Spam()
x.print_num_instances()
Sub.print_num_instances()

z = Other()
z.print_num_instances()