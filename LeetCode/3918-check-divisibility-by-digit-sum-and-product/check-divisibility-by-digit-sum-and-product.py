class Solution(object):
    def checkDivisibility(self, n):
        sum_num, mul_num = 0, 1

        m = n
        while m:
            num = m % 10
            m //= 10

            sum_num += num
            mul_num *= num

        if n % (sum_num + mul_num) == 0:
            return True
        else:
            return False