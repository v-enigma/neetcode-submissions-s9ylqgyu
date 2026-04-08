class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letterMap = {}
        def checkPermutation(left, right):
            dMap = { key : 0 for key in s1}
            isPermutation = True
            for i in range(left, left+len(s1)):
                dMap[s2[i]] = dMap[s2[i]] + 1
                if dMap[s2[i]] > letterMap[s2[i]]:
                    isPermutation = False

            if not isPermutation:
                last = left
                
                for i in range(left+len(s1), right):
                    dMap[s2[last]] = dMap[s2[last]] - 1
                    last = last+1 
                    dMap[s2[i]] = dMap[s2[i]] + 1
                    found = True
                    for key in letterMap.keys():
                        if letterMap[key] != dMap[key]:
                            found = False
                            break
                    if found:
                        return True
                return False
            else:
                return True                
        
        for i in s1:
            if i in letterMap.keys():
                letterMap[i] = letterMap[i]+1
            else:
                letterMap[i] = 1
        left = 0
        right = len(s2)
        intial = -1
        while left < right :
            if intial == -1 and  s2[left] in letterMap.keys():
                intial = left
            elif intial >= 0 and s2[left] not in letterMap.keys():
                print(s2[left])
                length = left-intial 
                if length == len(s1):
                    return True
                elif length > len(s1):
                    result = checkPermutation(intial,left)
                    if result:
                        return result
                    intial = -1
                else:
                    intial = -1
                    
            left = left + 1
        if intial >= 0 :
            return checkPermutation(intial,left)
        return False

                
        
        