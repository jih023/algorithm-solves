m = int(input())
n = int(input())
sum_num = 0
min_num = 0

i = 1
while True:
    if i * i >= m and i * i <= n:
        if not min_num:
            min_num = i * i
        sum_num += i * i
    elif i * i > n:
        break
    i += 1

if not sum_num:
    print(-1)
else:
    print(sum_num)
    print(min_num)