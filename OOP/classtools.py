"Смешанные утилиты и инструменты для классов"
class AttrDisplay:
    """
    Предоставляет наследуемый метод для перегрузки отображения, который показывакет
    экземпляры с их именами классов и пары имя=значение для каждого атрибута,
    сохраненного в самом экземпляре (но не атрибутов, унаследованных от его классов).
    Может соединяться с любым классом и будет работать на любом экземпляре.
    """
    def gatherAttrs(self):
        return ', '.join('{}={}'.format(key, getattr(self, key)) for key in sorted(self.__dict__))

    def __repr__(self):
        return '[{}: {}]'.format(self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2
    class SubTest(TopTest):
        pass
    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)
