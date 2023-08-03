d = {'spam': 2, 'ham': 1, 'eggs': 3}

# for k, v in d.items():
#     print('{}: {}'.format(k, v))

# d2 = {'toast': 4, 'muffin': 5}
# d.update(d2)
# print(d)


# movies = {
#     'Holy Grail': 1975,
#     'Life of Brian': 1979,
#     'The Meaning of Life': 1983,
# }
# print([title for (title, year) in movies.items() if year == 1979])


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")
# print(dict(zip(a, b)))


# print(dict.fromkeys(['a', 'b'], 0))


# D = dict(c=3, a=1, b=2)
# Ks = list(D)
# Ks.sort()
# [print(k, D[k]) for k in Ks]
# # or alternative use sorted on keys
# [print(k, D[k]) for k in sorted(D)]

# print({k: 0 for k in 'ab'})
# print(dict.fromkeys('ab', 0))


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

