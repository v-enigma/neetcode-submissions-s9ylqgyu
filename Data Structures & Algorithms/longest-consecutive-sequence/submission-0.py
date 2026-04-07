class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dataDict = {}
        maxCount = [0]
        for item in nums:
            dataDict[item] ="NotVisited"
        def leftBorder(number,count):
            if number not in dataDict:
                return count
            count = count+1
            dataDict[number] = "visited"
            return leftBorder(number-1, count)
        
        def rightBorder(number, count):
            if number not in dataDict:
                    return count
            count = count+1
            dataDict[number] = "visited"
            return rightBorder(number+1, count)

        def findConsecutive():
            for item in nums:
                
                if dataDict[item] != 'visited':
                    dataDict[item] = 'visited'
                    leftCount = leftBorder(item-1,0)
                    rightCount = rightBorder(item+1,0)
                    if maxCount[0] < (leftCount + rightCount + 1):
                        maxCount[0] = leftCount + rightCount + 1
            return maxCount[0]
        return findConsecutive()

            
            

            
        