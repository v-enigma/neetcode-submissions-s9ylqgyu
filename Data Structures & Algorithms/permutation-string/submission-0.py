class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letterMap = {}
        for i in s1:
            if i in letterMap.keys():
                letterMap[i] = letterMap[i]+1
            else:
                letterMap[i] = 1
        left = 0
        right = len(s2)
        intial = -1
        while left < right :
            if intial ==-1 and  s2[left] in letterMap.keys():
                intial = left
            elif intial > 0 and s2[left] not in letterMap.keys():
                length = left-intial 
                if length != len(s1):
                    intial = left
                else:
                    return True
            left = left + 1
        return False

                
        
        