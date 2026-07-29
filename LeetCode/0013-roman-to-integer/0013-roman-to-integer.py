class Solution(object):
    def romanToInt(self, s):
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = dict[s[0]]

        for i in range(1, len(s)):
            if (s[i] == 'V' or s[i] == 'X') and s[i - 1] == 'I':
                result -= 2
            if (s[i] == 'L' or s[i] == 'C') and s[i - 1] == 'X':
                result -= 20
            if (s[i] == 'D' or s[i] == 'M') and s[i - 1] == 'C':
                result -= 200
            result += dict[s[i]]
        
        return result