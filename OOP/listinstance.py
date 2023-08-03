class ListInstance:
    # def __attrnames(self):
    #     return ''.join('\t{}={}\n'.format(attr, self.__dict__[attr]) for attr in sorted(self.__dict__))
    # def __attrnames(self):
    #     result = ''
    #     for attr in dir(self):
    #         if attr[:2] == '__' and attr[-2:] == '__':
    #             result += '\t{}\n'.format(attr)
    #         else:
    #             result += '\t{}={}\n'.format(attr, getattr(self, attr))
    #     return result
    def __attrnames(self, indent=' '*4):
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82-(len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)

    def __str__(self):
        return '<Instance of {}, address {}:\n{}>'.format(
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )


if __name__ == '__main__':
    class Spam(ListInstance):
        def __init__(self):
            self.data1 = 'food'
    x = Spam()
    print(x)