# def rotate(self, nums, k):
#     print(nums[:-k], nums[k - 1:], sep="")
#
k = 3
nums = [1, 2, 3, 4, 5, 6, 7]
while k != 0:
    nums.insert(0, nums[-1])
    nums.pop()
    k -= 1
print(nums)
