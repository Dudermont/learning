def twoSum(nums, target):
    numDict = {}
    for i, j in enumerate(nums):
        x = target - j
        if x in numDict:
            return numDict[x], i
        else:
            numDict[j] = i


print(twoSum([2, 7, 11, 15], 9))
