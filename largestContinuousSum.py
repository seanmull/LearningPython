def large_cont_sum(arr):
    localMax = 0
    finalMax = 0
    for num in arr:
        localMax += num
        finalMax = max(localMax, finalMax)
        if localMax < 0:
            localMax = 0
    return finalMax

a = [1,2,-1,3,4,10,10,-10,-1]
print(large_cont_sum(a))