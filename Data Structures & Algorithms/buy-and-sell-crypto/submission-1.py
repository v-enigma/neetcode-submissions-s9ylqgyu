class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        intial = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] <= intial :
                intial = prices[i]
            else:
                profit = max(prices[i]-intial,profit)
        return profit
        
        