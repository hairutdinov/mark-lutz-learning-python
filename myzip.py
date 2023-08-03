# def myzip(*seqs):
#     res = []
#     for i in range(len(seqs[0])):
#         inner_res = []
#         for j in range(len(seqs)):
#             if len(seqs[j]) <= i:
#                 break
#             inner_res.append(seqs[j][i])
#         else:
#             res.append(inner_res)
#     return res
#    # return [[seq[i] if len(seq) > i else None for i in range(len(seq))] for seq in seqs]


# def myzip(*seqs):
#     seqs = [list(S) for S in seqs]
#     res = []
#     while all(seqs):
#         res.append(tuple(S.pop(0) for S in seqs))
#     return res

def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

print(myzip([11, 2, 4], [3, 22, 5]))
print(myzip('spam', 'ham'))