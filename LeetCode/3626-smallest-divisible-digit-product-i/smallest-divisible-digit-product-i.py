class Solution(object):
    def smallestNumber(self, n, t):
        num = n

        while True:
            mul_result = 1
            num = n

            while num > 0:
                digit = num % 10
                mul_result *= digit
                num //= 10
            
            if mul_result % t == 0:
                return n
            
            n += 1
                