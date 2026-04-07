class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [0]
        def findPaths(i:int, j:int) -> int:
            if i == m-1 and j == n-1 :
                count[0] = count[0]+1
                
            elif  i < m-1 and j < n-1:
                findPaths(i+1,j)
                findPaths(i,j+1)
            elif i == m-1:
                findPaths(i,j+1)
            elif j == n-1:
                findPaths(i+1,j)
            
        findPaths(0,0)
        return count[0]

             
            
            


                
        