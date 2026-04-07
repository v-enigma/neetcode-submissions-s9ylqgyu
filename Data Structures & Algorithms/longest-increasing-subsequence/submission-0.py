class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.dfs(nums, [], 0)
    def dfs(self, nums:List[int], bag : List[int], currentIndex) -> int:
        if currentIndex >= len(nums) :
            return len(bag)
        else:
            left  = -1
            include = True
            if len(bag) > 0 and bag[-1] >= nums[currentIndex] :
                include = False
            if include :
                temp = bag.copy()
                temp.append(nums[currentIndex])
                left = self.dfs(nums,temp,currentIndex+1)
            right = self.dfs(nums,bag,currentIndex+1)
            return max(left, right)
        
                


        

        

        