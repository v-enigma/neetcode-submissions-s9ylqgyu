class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights)-1
        while left < right:
            area = (right-left)*min(heights[left], heights[right])
            if area > result :
                result = area
            if heights[left]< heights[right]:
                left = left+1
            else:
                right = right -1
        return result
        