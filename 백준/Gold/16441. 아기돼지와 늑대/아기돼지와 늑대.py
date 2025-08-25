from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n, m = map(int, input().split())

arr = []
wolves = []
for i in range(n):
    line = list(input())
    for j, val in enumerate(line):
        if val == 'W':     
            wolves.append((i, j))
    arr.append(line)

visited = [[0] * m for _ in range(n)]

def bfs(x, y):
    global visited

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] or arr[nx][ny] == '#':
                continue

            while arr[nx][ny] == '+':
                mx, my = nx + dx[i], ny + dy[i]
                if 0 <= mx < n and 0 <= my < m:
                    if arr[mx][my] == '#':
                        break
                    else:
                        nx, ny = mx, my
                else:
                    break

            if not visited[nx][ny] and arr[nx][ny] != '#':
                visited[nx][ny] = 1
                q.append((nx, ny))

for i, j in wolves:
    bfs(i, j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == '.' and not visited[i][j]:
            arr[i][j] = 'P'

for r in arr:
    print("".join(map(str, r)))