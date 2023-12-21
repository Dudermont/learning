def productExceptSelf(nums):
    res = [0] * len(nums)

    perf = 1
    for i in range(len(nums)):
        res[i] = perf
        perf *= nums[i]

    lperf = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= lperf
        lperf *= nums[i]

    return res