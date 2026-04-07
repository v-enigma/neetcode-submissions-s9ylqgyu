class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        df = [0]*(len(cost)+1)
        df[0] = cost[0]
        df[1] = cost[1]
       
        for i in range(2,len(cost)+1):
            if i == len(cost):
                df[i] = min(df[i-1], df[i-2])
            else:
                df[i] = cost[i] + min(df[i-1], df[i-2])
        
        return df[len(cost)]


        