class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        noColumns = len(height[0])
        noRows = len(height)
        pac = set()
        atl = set()
        result = []
        def dfs(row, col, visited, prevHeight):
            if ((row , col) in visited or
             row <0 or col < 0 or row == noRows or col == noColumns or height[row][col] < prevHeight  ):
             return 
            visited.add((row,col))
            for i in range(-1,2):
                if i!= 0:
                    dfs(row+i, col,visited, height[row][col])
            for j in range(-1,2):
                if j!=0:
                    dfs(row, col+j, visited, height[row][col])
        for i in range(noRows):
            dfs(i,0,pac,height[i][0])
            dfs(i,noColumns-1,atl, height[i][noColumns-1])
        for i in range(noColumns):
            dfs(0,i,pac,height[0][i])
            dfs(noRows-1, i, atl,height[noRows-1][i])
        for i in range(noRows):
            mark = []
            for j in range(noColumns):
                if (i,j) in pac and (i,j) in atl :
                    result.append([i,j])
            
        return result



                    
                
                




        
        


        