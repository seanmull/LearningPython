from collections import Counter
import collections

l = [1,2,2,2,2,2,3,3,3,3]

print(Counter(l))

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print(Counter(words))

c = Counter(words)

# print(c.most_common(2))

# print(c.values())
# # print(c.clear())
# print(list(c))
# print(set(c))
# print(dict(c))

print ('Normal dictionary:')

d1 = {}

d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

for k, v in d1.items():
    print(k,v)


print ('OrderedDict:')

d = collections.OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print (k,v)