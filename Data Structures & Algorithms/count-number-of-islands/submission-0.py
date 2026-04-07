class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[-1 for i in range(len(grid[0]))] for j in range(len(grid)) ]
        ROWS = len(grid)
        COL = len(grid[0])

        count  = 0 
        def dfs(row, column):
            if row >=0 and row < ROWS and column < COL and column >= 0  and  visited[row][column] == -1:
                visited[row][column] = 1
                if grid[row][column] == '1':
                    dfs(row-1, column)
                    dfs(row+1, column)
                    dfs(row, column+1)
                    dfs(row, column-1)
        for i in range(ROWS):
            for j in range(COL):
                if grid[i][j] == '1' and visited[i][j] == -1 :
                    dfs(i, j)
                    count = count+1
        return count



              


        