class Solution(object):
    def sumAndMultiply(self, n):
        arr = list(str(n))
        x = "0"
        sum_n = 0
        for a in arr:
            if a != "0":
                x += a
            sum_n += int(a)

        return int(x) * sum_n