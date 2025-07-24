def to_base_n(num, base):
    digits = "01234567809"
    if num == 0:
        return "0"
    
    result = ''
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result

def check_palindrome(s):
    return s == s[::-1]

n = int(input())
flag = 1

for i in range(2, 10):
    num = to_base_n(n, i)
    if check_palindrome(num):
        print(i, num)
        flag = 0

if check_palindrome(str(n)):
    flag = 0
    print(10, n)
elif flag:
    print('NIE')