def search(nums, target):
    start = 0
    last = len(nums) - 1
    while start <= last:
        midl = (start + last) // 2
        if nums[midl] == target:
            return midl
        elif start == last:
            if nums[midl] < target:
                return midl + 1
            return start
        elif nums[midl] > target:
            if nums[midl - 1] < target < nums[midl]:
                return midl
            last = midl - 1
        else:
            start = midl + 1
    return 0


print(search([1, 3], 0))
