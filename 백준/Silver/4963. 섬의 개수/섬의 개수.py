from collections import deque

dx, dy = [0, 0, 1, -1, -1, 1, -1, 1], [1, -1, 0, 0, 1, 1, -1, -1]

while 1:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    land = [list(map(int, input().split())) for _ in range(h)]
    check = [[0] * w for _ in range(h)]
    cnt = 0

    q = deque()
    
    for i in range(h):
        for j in range(w):
            if not check[i][j] and land[i][j]:
                q.append((i, j))
                cnt += 1
            
            while q:
                x, y = q.popleft()
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1 and not check[nx][ny]:
                        check[nx][ny] = 1
                        q.append((nx, ny))
    
    print(cnt)