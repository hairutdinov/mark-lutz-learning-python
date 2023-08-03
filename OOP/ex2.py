from first_class import FirstClass
from second_class import SecondClass
from third_class import ThirdClass

x = FirstClass()
y = FirstClass()

x.set_data('King Arthur')
y.set_data(3.14159)

x.display()
y.display()

z = SecondClass()
z.set_data(42)
z.display()

a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()
print(b)

a.mul(3)
print(a)



class Rec:
    pass


def uppername(obj):
    return obj.name.upper()

Rec.method = uppername

Rec.name = 'Bob'
Rec.age = 32

x = Rec()
y = Rec()
x.name = 'Sue'

print('uppername method: ', x.method())

print(Rec.name, x.name, y.name)
print(list(Rec.__dict__.keys()))
print(list(k for k in Rec.__dict__.keys() if not k.startswith('__')))

print(x.name, x.__dict__['name'])
# print(x.age, x.__dict__.get('age'))

# print(uppername(x))

