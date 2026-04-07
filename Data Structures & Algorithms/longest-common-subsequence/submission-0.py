class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [ [0 for c in range(len(text1)+1)] for i in range(len(text2)+1)]
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                if text2[i-1] == text1[j-1]:
                    grid[i][j] = 1 + grid[i-1][j-1] 
                    
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        return grid[len(text2)][len(text1)]


        