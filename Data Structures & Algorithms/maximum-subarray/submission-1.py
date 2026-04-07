class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum , maxSum =0, nums[0]
        for i in range(0,len(nums)):
            currSum = max(currSum,0)
            currSum = currSum + nums[i]
            maxSum = max(currSum, maxSum)
        return maxSum

        