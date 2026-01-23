n = int(input())
m = int(input())
arr = input()

i, count, result = 0, 0, 0

while i < m - 2:
    if arr[i:i+3] == 'IOI':
        count += 1
        if count >= n:
            result += 1
        i += 2
    else:
        count = 0
        i += 1

print(result)