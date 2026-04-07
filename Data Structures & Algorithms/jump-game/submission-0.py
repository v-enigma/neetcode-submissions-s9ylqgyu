class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canReachEnd(index)->bool:
            if index < len(nums)-1 and nums[index] > 0:
                reached = False
                for i in range(index+1,index+nums[index]+1):
                    reached = reached or canReachEnd(i)
                return reached
            elif index == len(nums)-1:
                return True
            return False
    
        return canReachEnd(0)
        

        