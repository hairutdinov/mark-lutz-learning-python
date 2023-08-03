from person import Person


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus):
        self.person.give_raise(percent + bonus)

    def __repr__(self):
        return str(self.person)

    def __getattr__(self, attr):
        return getattr(self.person, attr)


if __name__ == '__main__':
    tom = Manager('Tom Jones', 50000)
    print(tom.name)
    print(tom.last_name())
    tom.give_raise(.10, .10)
    print(tom)
