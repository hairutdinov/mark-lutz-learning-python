from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

    # def action(self):
    #     # assert False, 'action must be defined!'
    #     # or
    #     raise NotImplementedError('action must be defined!')
    # or with abstract method
    @abstractmethod
    def action(self):
        pass


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    # pass
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print(klass.__name__ + '...')
        klass().method()
        print()
    print()
    x = Provider()
    x.delegate()
