class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_set = {}
        for i in s:
            if i in s_set:
                s_set[i] = s_set[i] + 1
            else:
                s_set[i] = 1
        for j in t:
            if j not in s_set or s_set[j] == 0 :
                return False
            s_set[j] = s_set[j] - 1
        return True
            

        