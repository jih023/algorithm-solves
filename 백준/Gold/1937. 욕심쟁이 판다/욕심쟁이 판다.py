import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline 

n = int(input())

bamboo = []
for _ in range(n):
    bamboo.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dp = [[0] * n for _ in range(n)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and bamboo[nx][ny] > bamboo[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    return dp[x][y]

max_cnt = 0
for i in range(n):
    for j in range(n):
        max_cnt = max(max_cnt, dfs(i, j))

print(max_cnt)