class Solution:
    def trap(self, height: List[int]) -> int:
       left = 0 
       right = len(height)-1
       leftmax = height[left]
       rightmax = height[right]
       accumulated = 0
       while left < right:
        if leftmax <= rightmax:
            left = left +1
            leftmax = max(height[left], leftmax )
            accumulated = accumulated + leftmax - height[left]
        else:
            right = right -1
            rightmax = max(height[right], rightmax)
            accumulated = accumulated + rightmax - height[right]
       return accumulated
        

            





        