s = 'hello'

print(s[1])
a = ""
for c in enumerate(s):
    a += s[-(c[0] + 1)]
print(a)

print(s[len(s) - 1])
print(s[-1])

way1 = [0,0,0]
way2 = [0 for w in range(0,3)]

print(way1)
print(way2)

l = [1,2,[3,4,'hello']]

l[2][2] = 'goodbye'

print(l)

d = {'simple key':'hello'}
print(d['simple key'])

d2={'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d4['k1'][2]['k2'][1]['tough'][2][0])

l4 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(l4) )

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#True or False?
print(l_one[2][0] >= l_two[2]['k1'])
