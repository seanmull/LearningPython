num = 1024
print(bin(num))
print(hex(num))

print(round(5.2322, 2))

s = 'hello how are you mary, are you felling okay?'

listOfLetter = [letter for letter in s if letter.isalpha() and letter != letter.lower()]
print(len(listOfLetter) == 0)

s1 = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'

print(s1.count('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1.difference(set2))

print(set1.union(set2))

dictOfNums = {n:pow(n,3) for n in range(0,5)}
print(dictOfNums)

l = [1,2,3,4]
(l.reverse())
print(l)
l2 = [3,4,2,5,1]
(l2.sort())
print(l2)