# class Squares:
#     def __init__(self, start, stop):
#         self.value, self.stop = start-1, stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value == self.stop:
#             raise StopIteration
#         self.value += 1
#         return self.value ** 2
# X = Squares(0, 5)
# print(next(X))
# # print(next(X))
# # print(next(X))
# # print(next(X))
# # print(next(X))
# # print(next(X))
# for i in X:
#     print(i, end=' ')


# class Squares:
#     def __init__(self, start, stop):
#         self.start, self.stop = start, stop
#     def __iter__(self):
#         for value in range(self.start, self.stop + 1):
#             yield value ** 2
# S = Squares(1, 5)
# I = iter(S)
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))
# for i in S:
#     print(i)

# class SkipObject:
#     def __init__(self, wrapped):
#         self.wrapped = wrapped
#     def __iter__(self):
#         return SkipIterator(self.wrapped)
# class SkipIterator:
#     def __init__(self, wrapped):
#         self.wrapped = wrapped
#         self.offset = 0
#     def __next__(self):
#         if self.offset >= len(self.wrapped):
#             raise StopIteration
#         else:
#             item = self.wrapped[self.offset]
#             self.offset += 2
#             return item
# alpha = 'abcdef'
# skipper = SkipObject(alpha)
# I = iter(skipper)
# print(next(I), next(I), next(I))
# for x in skipper:
#     for y in skipper:
#         print(x + y, end=' ')


