class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()

        result = []
        start, end = nums[0], nums[-1]

        if end - start + 1 != len(nums):
            idx = 0

            for i in range(start, end + 1):
                if nums[idx] != i:
                    result.append(i)
                else:
                    idx += 1
        
        return result