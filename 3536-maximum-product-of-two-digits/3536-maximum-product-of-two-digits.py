class Solution(object):
    def maxProduct(self, n):
        arr = list(str(n))
        arr.sort()
        return int(arr[-1]) * int(arr[-2])