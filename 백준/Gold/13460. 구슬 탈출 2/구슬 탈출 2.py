from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

q = deque()
q.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = 1

while q:
    rx, ry, bx, by, dist = q.popleft()

    if dist >= 10:  
        break

    for i in range(4): 
        nrx, nry, rmove = move(rx, ry, dx[i], dy[i])
        nbx, nby, bmove = move(bx, by, dx[i], dy[i])

        if board[nbx][nby] == 'O':
            continue
        if board[nrx][nry] == 'O':
            print(dist + 1)
            exit(0)

        if nrx == nbx and nry == nby:
            if rmove > bmove:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]

        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = 1
            q.append((nrx, nry, nbx, nby, dist + 1))

print(-1)