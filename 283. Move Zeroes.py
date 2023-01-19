def rotate(nums):
    k = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[k], nums[r] = nums[r], nums[k]
            k += 1
    return nums


num = [0, 1, 0, 3, 12]
print(rotate(num))
