class Solution(object):
    def maxProduct(self, nums):
        length = len(nums)
        max_result = 0
        for i in range(length - 1):
            for j in range(i+1, length):
                max_result = max(max_result, (nums[i] - 1) * (nums[j] - 1))
        return max_result
