class Solution:
    def numDecodings(self, s: str) -> int:
        
        def helper(index:int):
            if index == len(s):
                return 1
            elif index < len(s) and int(s[index]) in range(1,27):
                left = helper(index+1)
                right = 0
                if index+1 < len(s) and int(s[index:index+2]) in range(1,27):
                    right = helper(index+2)
                return left+right
            else : 
                return 0
        return helper(0)










        