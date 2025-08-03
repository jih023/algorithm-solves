n, m, r = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))

for c in cmd:
    if c == 1:
        for i in range(n // 2):
            arr[i][:], arr[-1-i][:] = arr[-1-i][:], arr[i][:]
    elif c == 2:
        for row in arr:
            for i in range(m // 2):
                row[i], row[-1 - i] = row[-1 - i], row[i]
    elif c == 3:
        n, m = m, n
        temp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[-j-1][i]
        arr = temp
    elif c == 4:
        n, m = m, n
        temp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[j][-i-1]
        arr = temp
    elif c == 5:
        for i in range(n // 2):
            arr[i][:m//2], arr[i][m//2:], arr[i+n//2][m//2:], arr[i+n//2][:m//2] = arr[i+n//2][:m//2], arr[i][:m//2], arr[i][m//2:], arr[i+n//2][m//2:]
    elif c == 6:
        for i in range(n // 2):
            arr[i][:m//2], arr[i][m//2:], arr[i+n//2][m//2:], arr[i+n//2][:m//2] = arr[i][m//2:], arr[i+n//2][m//2:], arr[i+n//2][:m//2], arr[i][:m//2]

for r in arr:
    for c in r:
        print(c, end=" ")
    print()