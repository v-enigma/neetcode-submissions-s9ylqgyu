class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]* (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i >= j and dp[i- j] != float('inf'):
                    dp[i] = min((1+ (dp[i-j])), dp[i])
        if dp[amount] == float('inf'):
            return -1
        else :
            return dp[amount]

        