from math import pi
from functools import reduce

def vol(rad):
    return (4/3) * pi * pow(rad, 3) 

# print(vol(3))

def ran_check(num,low,high):
    return num in range(low,high+1)

print(ran_check(3,1,10))

s = "Hello Mr. Rogers, how are you this fine Tueday?"

def up_low(s):
    # up = len([char for char in s if char.isupper()])
    lower = len([char for char in s if char.islower()])
    print("No. of Upper case characters:", up) 
    print("No. of Lower case characters:", lower) 

print(up_low(s))

l = [1,1,1,1,1,2,2,2,2,3,3,3,3,4,5]

def unique_list(l):
    s = set(l)
    return list(s)

print(unique_list(l))

l2 = [1,2,3,-4]

def multiply(l):
    return reduce(lambda x,y : x * y,  l)

print(multiply(l2))


s2 = 'hh'
def palindrome(s):
    if len(s) == 1 or len(s) == 0: return True
    lo = 0
    hi = len(s) - 1
    while(hi > lo and s[lo] == s[hi]):
        lo += 1
        hi -= 1
    return lo > hi

print(palindrome(s2))



