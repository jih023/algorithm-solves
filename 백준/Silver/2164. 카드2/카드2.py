n = int(input())

arr = list(range(1, n+1))
idx = 0

while idx != len(arr) - 1:
    idx += 1
    arr.append(arr[idx])
    idx += 1

print(arr[idx])