class Spam:
    num_instances = 0
    def __init__(self):
        Spam.num_instances += 1
    def print_num_instances():
        print(f'Number of instances created: {Spam.num_instances}')

    print_num_instances = staticmethod(print_num_instances)

class Other(Spam): pass

a = Spam()
b = Spam()
Spam.print_num_instances()
b.print_num_instances()

c = Other()
c.print_num_instances()