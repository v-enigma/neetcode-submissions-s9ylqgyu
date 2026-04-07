class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def rob2(nums: List[int]) -> int:
            rob1 , rob2 = 0,0
            for n in nums:
                newrob = max(rob2, n+ rob1)
                rob1 = rob2
                rob2 = newrob
            return rob2
        return max(nums[0],rob2(nums[:-1]),rob2(nums[1:]))


        


        