import sys
sys.setrecursionlimit(30000)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

dp = [[-1] * n for _ in range(m)]

def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1  

    if dp[x][y] != -1:
        return dp[x][y]  

    dp[x][y] = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))