# f = open('myfile.txt', 'w')
# f.write('hello text file\n')
# f.write('goodbye text file\n')
# f.close()
# f = open('myfile.txt')
# print(f.readline())
# print(f.readline())
# print(f.readline())


# print(open('myfile.txt').read())

# pickle
# D = {'a': 1, 'b': 2, 'c': 3}
# F = open('datafile.pkl', 'wb')
# import pickle
# pickle.dump(D, F)
# F.close()

# F = open('datafile.pkl', 'rb')
# E = pickle.load(F)
# print(E)


X = 1
Y = 2
X, Y = Y, X
print(X, Y)

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'])
import json
# S = json.dumps(rec)
# O = json.loads(S)
# json.dump(rec, fp=open('testjson.json', 'w'), indent=4)
# P = json.load(open('testjson.json'))
# print(P)

