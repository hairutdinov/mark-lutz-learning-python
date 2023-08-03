def classtree(cls, indent=0, visited=None):
    if visited is None:
        visited = set()
    if cls.__name__ in visited and cls.__name__ != 'object':
        return
    visited.add(cls.__name__)
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent+3, visited)

def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass
    instancetree(B())
    instancetree(F())

if __name__ == '__main__':
    selftest()