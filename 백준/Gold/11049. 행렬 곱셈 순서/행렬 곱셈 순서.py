n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

for length in range(1, n):
    for i in range(n - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])