# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        start = 1
        last = n
        while start < last:
            midl = (start + last) // 2
            if isBadVersion(midl):
                last = midl
            else:
                start = midl + 1
        return last
