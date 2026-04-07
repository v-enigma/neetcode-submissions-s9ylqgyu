class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        df = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
           df[i] = min(df[i-1]+cost[i-1], df[i-2]+cost[i-2])
        
        return df[len(cost)]


        