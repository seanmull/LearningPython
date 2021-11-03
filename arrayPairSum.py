def pair_sum(nums, target):
    numsAlreadyLookedAt = set() 
    pairsThatSumToTarget = []
    for num in nums:
        remainder = target - num
        if remainder in numsAlreadyLookedAt:
            pair = (num, remainder)
            pairsThatSumToTarget.append(pair)
        numsAlreadyLookedAt.add(num)
    return len(pairsThatSumToTarget)

print(pair_sum([1,3,2,2], 4))