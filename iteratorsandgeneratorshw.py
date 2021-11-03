from random import randint
def gensquares(N):
    for n in range(N):
        yield pow(n,2)

# for x in gensquares(10):
#     print(x)

def rand_num(low,high,n):
    for val in range(n):
        yield randint(low,high)
    
for num in rand_num(1,10,12):
    print(num)