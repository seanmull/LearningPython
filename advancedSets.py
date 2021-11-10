s = set()

s.add(1)
s.add(2)
print(s)

s.clear()

s = {1,2,3}
sc = s.copy()

print(sc)
s.add(4)
print(s)
print(sc)

print(s.difference(sc))

s.discard(2)

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

print(s1.issubset(s2))
print(s2.issuperset(s1))

print(s1.union(s2))

