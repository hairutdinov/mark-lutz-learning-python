# class Indexer:
#     def __getitem__(self, index):
#         return index ** 2
#
# X = Indexer()
# print(X[4])


# class Indexer:
#     data = [5, 6, 7, 8, 9]
#     def __getitem__(self, index):
#         print('getitem:', index)
#         return self.data[index]
#
# X = Indexer()
# print(X[0])
# print(X[-1])
# print(X[1::2])


# class Indexer:
#     data = [5, 6, 7, 8, 9]
#     def __getitem__(self, index):
#         if isinstance(index, int):
#             print('indexing', index)
#         else:
#             print('slicing', index.start, index.stop, index.step)
#
# X = Indexer()
# X[0]
# X[-1]
# X[1::2]


# class StepperIndex:
#     def __getitem__(self, idx):
#         return self.data[idx]
#
# X = StepperIndex()
# X.data = 'spam'
# for item in X:
#     print(item)
