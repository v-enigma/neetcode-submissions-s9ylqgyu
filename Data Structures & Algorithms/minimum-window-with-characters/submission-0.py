class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Count frequency of each char in t
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        
        needed = len(tMap)  # Number of unique chars we need
        have = 0  # Number of unique chars we currently have with correct frequency
        
        sMap = {}  # Frequency map for current window
        left = 0
        minLen = float('inf')
        minLeft = 0
        
        for right in range(len(s)):
            # Add char from right to window
            c = s[right]
            sMap[c] = sMap.get(c, 0) + 1
            
            # Check if this char's frequency now matches what we need
            if c in tMap and sMap[c] == tMap[c]:
                have += 1
            
            # Contract window from left while valid
            while have == needed:
                # Update result if this window is smaller
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    minLeft = left
                
                # Remove char from left
                leftChar = s[left]
                sMap[leftChar] -= 1
                if leftChar in tMap and sMap[leftChar] < tMap[leftChar]:
                    have -= 1
                left += 1
        
        return "" if minLen == float('inf') else s[minLeft:minLeft + minLen]