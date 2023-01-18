def rotate(nums, k):
    k = k % len(nums)
    nums.reverse()
    a, b = 0, k - 1
    while a < b:
        nums[a], nums[b] = nums[b], nums[a]
        a += 1
        b -= 1
    a, b = k, len(nums) - 1
    while a < b:
        nums[a], nums[b] = nums[b], nums[a]
        a += 1
        b -= 1
    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
