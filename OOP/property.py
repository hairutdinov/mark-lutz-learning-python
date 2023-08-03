# class operators:
#     def __getattr__(self, item):
#         if item == 'age':
#             return 25
#         else:
#             raise AttributeError(item)
#
# x = operators()
# print(x.age)
# # print(x.name)

class properties(object):
    def get_age(self):
        return 25
    def set_age(self, value):
        print(f'set age: {value}')
        self._age = value
    age = property(get_age, set_age, None, None) # get, set, delete, doc string

x = properties()
print(x.age)
x.age = 29