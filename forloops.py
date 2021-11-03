l = [1,2,3,34,4,5,66]

for num in l:
    if num % 2 == 0:
        print(num)
    else:
        print("Odd number")
        

s = "This is the winter of our discontent"

for letter in s:
    print(letter)

l2 = [(2,4), (6,8), (10,12)]

for(t1,t2) in l2: #tuple unpacking
    print(t1)

d = {'k1': 1, 'k2': 2, 'k3' : 3}

for item in d.items():
    print (item)