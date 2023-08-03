class ListTree:
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += f'{spaces}{attr}\n'
            else:
                result += '{}{}={}\n'.format(spaces, attr, getattr(obj, attr))
        return result

    def __listclass(self, a_class, indent: int = 0):
        dots = '.' * indent
        if a_class in self.__visited:
            return '\n{}<Class {}: address: {} (see above)>\n'.format(
                dots,
                a_class.__name__,
                id(a_class)
            )
        else:
            self.__visited[a_class] = True
            here = self.__attrnames(a_class, indent)
            above = ''
            for super in a_class.__bases__:
                above += self.__listclass(super, indent + 4)
            return '\n{0}<Class: {1}, address: {2}\n{3}{4}{5}>\n'.format(
                dots,
                a_class.__name__,
                id(a_class),
                here,
                above,
                dots
            )

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address: {1}\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            here, above
        )


if __name__ == '__main__':
    class A(ListTree):
        def __init__(self):
            self.data_a_1 = 'spam'


    class B(A):
        def __init__(self):
            A.__init__(self)
            self.data_b_1 = 'eggs'


    class C(A):
        def __init__(self):
            A.__init__(self)
            self.data_c_1 = 'apple'


    class D(B, C):
        def __init__(self):
            B.__init__(self)
            C.__init__(self)
            self.data_d_1 = 'tomato'


    class E(ListTree):
        def __init__(self):
            self.data_e_1 = 'toast'


    class F(D, E):
        def __init__(self):
            D.__init__(self)
            E.__init__(self)
            self.data_f_1 = 'food'


    x = F()
    print(x)

