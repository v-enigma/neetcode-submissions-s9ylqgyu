class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphNum = []
        for i in s:
            if i.isalnum():
                alphNum.append(i.lower())
        #print(alphNum)
        return alphNum == alphNum[::-1]
        