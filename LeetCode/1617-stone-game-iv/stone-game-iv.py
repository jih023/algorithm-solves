class Solution(object):
    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)

        for s in range(1, n + 1):
            square = 1

            while square * square <= s:
                if not dp[s - square * square]:
                    dp[s] = True
                    break
                
                square += 1
        
        return dp[n]