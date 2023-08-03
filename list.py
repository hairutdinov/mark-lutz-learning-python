print(list(map(ord, 'spam')))

print([1, 2] + list(map(int, '34')))

L = [1, 2, 3, 4, 5]
# L[1:3] = L[:2]

# replace one element with 2
# L[1:2] = [22, 23]

# insert
# L[1:1] = [1.25, 1.5]

# delete
# L[1:3] = []

# print(L)

# print([0] * 5)
# print([0 for _ in range(5)])


# L2 = [4, 5, 6]
# X2 = L2 * 4
# Y2 = [L2] * 4
# Y2 = [L2[:]] * 4
# Y2 = [list(L2) for _ in range(4)]
# L2[0] = 44
# Y2[0][0] = 44
# print(X2)
# print(Y2)

print((1,) + (4, 5, 6)[1:])
