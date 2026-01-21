arr = list(input())
num = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
ans = [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]

total = 0
for i in range(13):
    if arr[i] != '*':
        total += num[i] * int(arr[i])
    else:
        star = num[i]

n = (10 - (total % 10)) % 10
if star == 1:
    print(n)
else:
    print(ans[n])