class Solution(object):
    def removeElement(self, nums, val):
        cnt = 0
        
        length = len(nums)
        for i in range(length):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt += 1
        
        return cnt