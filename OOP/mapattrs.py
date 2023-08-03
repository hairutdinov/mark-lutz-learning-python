"""
Файл mapattrs.py (Python 3.X + 2.X)
Главный инструмент: mapattrs () отображает все собственные
и унаследованные атрибуты экземпляра на экземпляр или класс, из которого они унаследованы.
Предполагает, что dir () выдает все атрибуты экземпляра.
Для эмуляции наследования использует либо кортеж MRO класса,
который дает порядок поиска для классов нового стиля (и всех классов в Python 3.X),
либо рекурсивный обход для выведения порядка DELR классических классов в Python 2.X.
Также здесь: inheritance () дает нейтральный к версии порядок следования классов;
различные словарные инструменты, использующие включения Python 3.X/2.7.
"""
import pprint


def trace(X, label='', end='\n'):
    print(label + pprint.pformat(X) + end)  # Симпатичный вывод


def filterdictvals(D, V):
    """
    Словарь D с элементами после удаления значения V.
    filterdictvals(dict(a=1, b=2, c=1), 1) => {'b': 2}
    """
    return {key: value for key, value in D.items() if value != V}


def invertdict(D):
    """
    Словарь D со значениями, измененными на ключи (сгруппированными по значениям).
    Все значения должны быть хешируемыми, чтобы работать как ключи словаря/множества.
    invertdict(dict(a=1, b=2, c=1)) => (1:['a', 'c'], 2:['b'])
    """
    def keysof(V):
        return sorted([k for k in D.keys() if D[k] == V])
    return {value: keysof(value) for value in set(D.values())}


def dflr(cls):
    """
    Классический порядок сначала в глубину, затем слева направо в дереве классов cls.
    Циклы невозможны: Python запрещает изменения в __bases__.
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here


def inheritance(instance):
    """
    Порядок поиска при наследовании: нового стиля (MRO) или классический (DFLR)
    """
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)


def mapattrs(instance, withobject=False, bysource=False):
    """
    Словарь с ключами, дающими все унаследованные атрибуты экземпляра,
    и значениями, содержащими обьекты, от которых унаследован каждый атрибут.
    withobject: False-удалить встроенные атрибуты класса object.
    bysource: True=сгруппировать результат по объектам, а не атрибутам.
    Поддерживает классы со слотами, которые препятствуют наличию __dict__
    в экземплярах.
    """
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:  # слоты
                attr2obj[attr] = obj
                break
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)


if __name__ == '__main__':
    class A: attr1 = 1
    class B(A): attr2 = 2
    class C(A): attr1 = 3
    class D(B, C): pass

I = D()
print('Py=>%s' % I.attr1)
trace(inheritance(I), 'INH\n')
trace(mapattrs(I), 'ATTRS\n')
trace(mapattrs(I, bysource=True), 'OBJS\n')
