# def mysum(l):
#     return l[0] if len(l) == 1 else l[0] + mysum(l[1:])
# def mysum(l):
#     first, *rest = l
#     return first if not rest else first + mysum(rest)
# print(mysum([1, 2, 3]))


# def sumtree(L):
#     total = 0
#     for x in L:
#         total += sumtree(x) if isinstance(x, list) else x
#     return total
# print(sumtree([1, [2, [3, 4], 5], 6, [7, 8]]))

# queue / очередь / обход в ширину / first in first out / FIFO
# def sumtree(L):
#     total = 0
#     items = list(L)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):
#             total += front
#         else:
#             items.extend(front)
#     return total
# print(sumtree([1, [2, [3, 4], 5], 6, [7, 8]]))

# стек / обход в глубину / last in first out / LIFO
# def sumtree(L):
#     total = 0
#     items = list(L)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):
#             total += front
#         else:
#             items[:0] = front
#     return total
# print(sumtree([1, [2, [3, 4], 5], 6, [7, 8]]))


# import sys
# print(sys.getrecursionlimit())



