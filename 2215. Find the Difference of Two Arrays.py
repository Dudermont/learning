def findDifference(nums1, nums2):
    r = list(set(nums1) - set(nums2))
    d = list(set(nums2) - set(nums1))
    return [r, d]
