class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum , maxSum =0, nums[0]
        for i in nums:
            currSum = max(currSum,0)
            currSum = currSum + i
            maxSum = max(currSum, maxSum)
        return maxSum

        