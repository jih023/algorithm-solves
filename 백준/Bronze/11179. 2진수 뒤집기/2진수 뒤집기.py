n = int(input())
str_n = str(bin(n))[-1:1:-1]
print(int(str_n, 2))