# L = [
#     {'name': 'Ivan', 'age': 19},
#     {'name': 'Petr', 'age': 29},
# ]
# print(list(map(lambda x: x['age'], L)))


# from functools import reduce
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
# print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))


# M = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# print([M[i][i] for i in range(len(M))])
# print([M[i][len(M[i]) - 1 - i] for i in range(len(M))])
# print([[col + 10 for col in row] for row in M])
