dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

r, c = map(int, input().split())

apb = []
for _ in range(r):
    apb.append(list(input()))

def dfs(x, y, string, cnt):
    global max_cnt
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if apb[nx][ny] not in string:
                max_cnt = max(max_cnt, cnt + 1)
                dfs(nx, ny, string + apb[nx][ny], cnt + 1)

max_cnt = 1
cnt = 1
string = str(apb[0][0])
dfs(0, 0, string, cnt)
print(max_cnt)