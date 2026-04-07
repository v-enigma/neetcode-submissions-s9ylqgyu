class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterMap = {}
        mostfrequent = -1
        left = 0
        right = len(s)
        intial = 0
        maxLength = 0
        while left < right :
            
            if letterMap.get(s[left],-1)!=-1 :
                letterMap[s[left]] = letterMap[s[left]] +1
                
            else:
                letterMap[s[left]] = 1
            if mostfrequent == -1:
                    mostfrequent = s[left]
            elif mostfrequent != -1 or mostfrequent!= s[left]:
                    if letterMap[mostfrequent] < letterMap[s[left]]:
                        mostfrequent = s[left]
            
            while intial < left and ( left - intial+1 - letterMap[mostfrequent] ) > k:
                print(left,intial)
                
                if letterMap[s[intial]] > 0:
                    letterMap[s[intial]]= letterMap[s[intial]]-1
                intial = intial + 1
                maxfreq = -1
                for i in letterMap.items():
                    if maxfreq == -1 :
                        if i[1] > 0:
                            maxfreq = i[1]
                            mostfrequent = i[0]
                    elif letterMap[mostfrequent]<= i[1]:
                        print(left,intial)
                        mostfrequent = i[0]
            maxLength = max(maxLength, left-intial+1 )
            left = left+ 1
        return maxLength
            

            


        
        