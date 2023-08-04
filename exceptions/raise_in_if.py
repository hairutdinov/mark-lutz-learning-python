class Failure(Exception): pass
def searcher(l, value):
    if value in l:
        return value
    else:
        raise Failure

search_value = 4
search_list = [1, 2, 3]
try:
    value = searcher(search_list, search_value)
except Failure:
    print(f'value {search_value} not found in {search_list}')
