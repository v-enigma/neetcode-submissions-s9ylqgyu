class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        last = nums[0]
        lastbefore = max(nums[1], nums[0])
        for i in range(2,len(nums)):
            lastbefore ,last = max( last+ nums[i], lastbefore), lastbefore

        return max(lastbefore,last)


        


        