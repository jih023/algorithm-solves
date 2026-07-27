class Solution(object):
    def isPalindrome(self, x):
        arr = list(str(x))

        flag = 1
        for i in range(len(arr)//2):
            if arr[i] != arr[-i-1]:
                flag = 0
        
        if flag:
            return True
        else:
            return False
        