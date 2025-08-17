from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(int(input())):
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    
    cnt = 0
    check = [[0] * w for _ in range(h)]

    q = deque()
    for i in range(h):
        for j in range(w):
            if check[i][j] == 0 and grid[i][j] == '#':
                cnt += 1
                check[i][j] = 1

                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == '#' and not check[nx][ny]:
                            check[nx][ny] = 1
                            q.append((nx, ny))
    
    print(cnt)