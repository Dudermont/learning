def sortedSquares(nums):
    start = 0
    end = len(nums) - 1
    squ = [0] * len(nums)
    count = end
    while start <= end:
        if nums[start] ** 2 > nums[end] ** 2:
            squ[count] = nums[start] ** 2
            start += 1
        else:
            squ[count] = nums[end] ** 2
            end -= 1
        count -= 1
    return squ


print(sortedSquares([-7, -3, 2, 3, 11]))
