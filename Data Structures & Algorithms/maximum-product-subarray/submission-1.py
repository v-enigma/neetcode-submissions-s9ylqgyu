class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProduct = nums[0]
        maxProduct = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            n = nums[i]
            probables  = (n, n* minProduct, n* maxProduct)
            minProduct, maxProduct = min(probables), max(probables)
            result = max(result, maxProduct)
        return result
        
            
        