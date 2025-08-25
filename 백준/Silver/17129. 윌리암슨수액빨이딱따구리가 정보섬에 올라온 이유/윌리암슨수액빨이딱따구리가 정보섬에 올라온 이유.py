from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n, m = map(int, input().split())

a = []
q = deque()
for i in range(n):
    num = list(map(int, input()))
    if 2 in num:
        ix, iy = i, num.index(2)
    a.append(num)

check = [[0] * m for _ in range(n)]

check[ix][iy] = 1
q.append(((ix, iy), 0))

while q:
    (pos, dist) = q.popleft()
    x, y = pos

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny] and a[nx][ny] != 1:
            if a[nx][ny] == 0:
                check[nx][ny] = 1
                q.append(((nx, ny), dist + 1))
            else:
                print("TAK")
                print(dist + 1)
                exit(0)

print("NIE")