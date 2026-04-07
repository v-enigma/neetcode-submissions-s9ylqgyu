class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMaps = {}
        initial = -1
        maxLength = 0
        for i in range(len(s)):
            if s[i] in charMaps:
                if initial <= charMaps[s[i]]:
                    initial = charMaps[s[i]]+1
                charMaps[s[i]] = i
                
            else:
                charMaps[s[i]] = i
                if initial == -1:
                    initial = i
                
            maxLength = max(i-initial+1, maxLength)
        return maxLength




        