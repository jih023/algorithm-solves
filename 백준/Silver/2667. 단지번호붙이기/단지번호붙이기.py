from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

q = deque()
visited = [[0] * n for _ in range(n)]

cnt = 0
result = []

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and not visited[i][j]:
            visited[i][j] = 1
            q.append((i, j))
            cnt_num = 1
            while q:
                x, y = q.popleft()
                num = arr[x][y]
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == num and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            cnt_num += 1
                            q.append((nx, ny))
            result.append(cnt_num)
            cnt += 1

print(cnt)
result.sort()
for i in result:
    print(i)