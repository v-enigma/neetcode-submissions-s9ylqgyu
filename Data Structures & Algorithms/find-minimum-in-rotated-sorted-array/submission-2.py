class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right  = len(nums)-1
        if len(nums) == 2:
            return min (nums[0], nums[1])
        while left <= right :
            middle = (left + right )//2
            if nums[left]>= nums[middle] <= nums[right]:
                print("Case 1")
                if right - left <2:
                    return nums[middle]
                    
                else:
                    if nums[middle-1] > nums[middle] < nums[middle+1]:
                        return nums[middle]
                    else:
                        right = middle -1
            elif nums[left]<= nums[middle] > nums[right]:
                print("Case 2")
                left = middle + 1
            elif  nums[left] < nums[middle] <= nums[right]:
                print("Case 3")
                right = middle - 1
        return -1





        