
print('That is %d %s bird!' % (1, 'dead'))
print('That is {0} {1} bird!'.format(1, 'dead'))

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})


food = 'spam'
qty = 10
print('%(qty)d more %(food)s' % vars())

print('{motto}, {0} and {food}'.format('ham', motto='spam', food='eggs'))

print('{}, {} and {}'.format('ham', 'spam', 'eggs'))

import sys
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))

some_list = list('SPAM')
parts = some_list[0], some_list[-1], some_list[1:3]
print('first={}, last={}, middle={}'.format(*parts))

print('{:,d}'.format(9999999))


