l = [1,2,3]
l.append(4)
print(l)
print(l.count(10))

x = [1,2,3]
x.append([4,5])
print(x)
x.remove([4,5])
x.extend([4,5])
print(x)

print(l.index(2))

l.pop()
print(l)

l.reverse()
print(l)