nums = range(20)

def even_check(num):
    if num%2 == 0:
        return True

# for num in filter(even_check, nums):
    # print(num)

for num in filter(lambda x : x%2==0, nums):
    print(num)