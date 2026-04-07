class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1)
        for i, key in enumerate(dp):
            if i == 0:
                continue
            minCoins = float('inf')
            for j in coins:

                if i >= j :
                    leftOver = i - j
                    count = 0
                    if dp[leftOver]>=0:
                        count = 1 + dp[leftOver]
                        if minCoins > count:
                            minCoins = count
            if minCoins == float('inf'):
                dp[i] = -1
            else :   
                dp[i] = minCoins
        return dp[amount]






        