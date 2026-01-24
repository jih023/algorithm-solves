from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            x2, y2 = i, j

result = [[0] * m for _ in range(n)]
result[x2][y2] = 0

q = deque()
q.append((x2, y2))
visited = [[0] * m for _ in range(n)]
visited[x2][y2] = 1

while q:
    x, y = q.popleft()
    num = result[x][y]
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny]:
            visited[nx][ny] = 1
            result[nx][ny] = num + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if not result[i][j] and arr[i][j] and not (x2 == i and y2 == j):
            result[i][j] = -1

for r in result:
    print(" ".join(map(str, r)))