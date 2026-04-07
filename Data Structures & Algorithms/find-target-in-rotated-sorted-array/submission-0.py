class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot():
            left = 0
            right = len(nums)-1
            while left < right :
                middle = (left + right)//2
                print(middle)
                if nums[middle ] >= nums[right] :
                    left = middle + 1
                else:
                    right = middle
            return left

        def binarySearch(left, right ):
            while left <= right :
                middle = (left + right)//2
                if nums[middle] == target:
                    return middle
                elif nums[middle]> target :
                    right = middle -1
                else :
                    left = middle + 1
            return -1
        pivot = findPivot()
        result1 = binarySearch(0, pivot-1)
        if result1 == -1:
            return binarySearch(pivot, len(nums)-1)
        else:
            return result1

        