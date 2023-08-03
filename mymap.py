# def mymap(func, *seqs):
#     res = []
#     for args in zip(*seqs):
#         res.append(func(*args))
#     return res
def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))
G = mymap(pow, *[[2, 3, 4, 5]] * 2)
print(list(G))
