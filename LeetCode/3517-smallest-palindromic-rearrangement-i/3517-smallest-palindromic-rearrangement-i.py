class Solution(object):
    def smallestPalindrome(self, s):
        length = len(s)
        arr = s[:length//2]
        arr = sorted(s[:length // 2])

        if length % 2 == 0:
            return ''.join(arr + arr[::-1])
        else:
            return ''.join(arr + [s[length // 2]] + arr[::-1])