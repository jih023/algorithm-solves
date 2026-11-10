def solution(m, n, puddles):
    mod = 1_000_000_007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    blocked = {(x, y) for x, y in puddles}
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in blocked or (x, y) == (1, 1):
                continue
            
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % mod
    
    return dp[n][m]