def search(nums, target):
    start = 0
    last = len(nums) - 1
    while start <= last:
        midl = (start + last) // 2
        if nums[midl] == target:
            return midl
        elif nums[midl] > target:
            last = midl - 1
        else:
            start = midl + 1
    return -1
