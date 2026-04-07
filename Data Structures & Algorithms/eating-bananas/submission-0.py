from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = 0
        for i in piles:
            if i > right :
                right = i
        left = 1
        def noOfHours(rate):
            totalHours = 0
            for i in piles:
                totalHours = totalHours + ceil(i/rate)
            return totalHours
        result = -1
        while (left <= right ):
            middle = (left + right)//2
            hours =noOfHours(middle)
            if  h >= hours:
                result = middle
                right = middle -1
                
            else:
                left = middle+1
        return result
        
            
            
            

        