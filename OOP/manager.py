from person import Person


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)

if __name__ == '__main__':
    tom = Manager('Tom Jones', 100000)
    tom.give_raise(.10)
    print(tom)
