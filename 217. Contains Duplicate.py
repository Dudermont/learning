def containsDuplicate(nums):
    r = set(nums)
    return len(r) < len(nums)


print(containsDuplicate([1, 2, 3, 1]))
