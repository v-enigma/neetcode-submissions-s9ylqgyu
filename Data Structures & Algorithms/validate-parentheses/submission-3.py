class Solution:
    def isValid(self, s: str) -> bool:
        sta =[]
        for k in range(len(s)):
            i = s[k]
            if i == "[" or i == '{' or i == '(':
                sta.append(i)
            else:
                if len(sta) > 0 and ((i == '}' and sta[-1] == '{' ) or (i == ')' and sta[-1] =="(") or ( i ==']' and sta[-1] == '[')):
                    sta.pop()
                else:
                    return False
        return len(sta) ==0

        