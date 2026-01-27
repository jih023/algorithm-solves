n = int(input())
home = []
for _ in range(n):
    home.append(list(map(int, input().split())))

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if home[i][j]:
            continue

        if j - 1 >= 0:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
        if i - 1 >= 0:
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        if i - 1 >= 0 and j - 1 >= 0 and not home[i-1][j] and not home[i][j-1]:
            dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])