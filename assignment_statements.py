# a, b, c, d = 'spam'

# a, *b = 'spam'
# print(a)
# print(b)


string = 'spam'
# a, b, c = list(string[:2]) + [string[2:]]
# --- OR ---
# a, b = string[:2]
# c = string[2:]
# --- OR ---
# ((a, b), c) = string[:2], string[2:]
# print(a)
# print(b)
# print(c)


# list_of_ips = [
#     ('192.168.0.1', 'localhost'),
#     ('127.0.0.1', 'localhost'),
#     ('172.0.0.18', 'vipnet'),
# ]
#
# for (ip, name) in list_of_ips:
#     print('Ip: {ip}; name: {name}'.format(ip=ip, name=name))


# L = [1, 2, 3, 4]
# while L:
#     front, L = L[0], L[1:]
#     or even easier
#     front, *L = L
#     print('front: {}, L: {}'.format(front, L))


# first_letter, *middle, last_letter = 'ambition'
# print(first_letter)
# print(''.join(middle))
# print(last_letter)


# f = open('test_print_to_file.txt', 'w')
# print('Hello', [1, 2, 3], 3.14, file=f)
# f.close()


# import sys
# sys.stdout.write(open('myfile.txt', 'r').read())
# sys.stdout = open('log.txt', 'a')
# print([1,2,3,4])


# import sys
# temp = sys.stdout
# sys.stdout = open('log.txt', 'a')
# print('spam')
# print(1, 2, 3)
# sys.stdout.close()
# sys.stdout = temp
# print('back here!')



