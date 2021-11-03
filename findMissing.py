def finder(arr1, arr2):
    a = set(arr1)
    b = set(arr2)
    yield a.difference(b)

a = [1,2,3,4,5,6,7,56,4564]
b = [3,7,2,1,4,6]
gen = finder(a,b)

print(finder(a,b))

for ele in gen:
    gen
    if(ele != 56):
        print(ele)

