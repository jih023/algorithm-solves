from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())

arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

check = [[0] * m for _ in range(n)]
val = 1
max_count = 0

q = deque()

for i in range(n):
    for j in range(m):
        if check[i][j] == 0 and arr[i][j] == 1:
            check[i][j] = val
            q.append((i, j))
            count = 1

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not check[nx][ny]:
                        check[nx][ny] = val
                        count += 1
                        q.append((nx,ny))
            val += 1 
            max_count = max(max_count, count)

print(val - 1)
print(max_count)