class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridMap = {}
        rowMap = {}
        columnMap = {}
        for i in range(9):
            for j in range(9):
                if board[i][j]!= ".":
                    if rowMap.get(i) :
                        if board[i][j] in rowMap.get(i) :
                            return False
                        else:
                            rowMap.get(i).add(board[i][j])
                    else:
                        rowMap[i] = set()
                        rowMap[i].add(board[i][j])
                    if columnMap.get(j):
                        if board[i][j] in columnMap.get(j) :
                            return False
                        else:
                            columnMap.get(j).add(board[i][j])
                    else:
                        columnMap[j] = set()
                        columnMap[j].add(board[i][j])
                    if gridMap.get((i//3, j//3)):
                        if board[i][j] in gridMap.get((i//3,j//3)):
                            return False
                        else:
                            gridMap.get((i//3, j//3)).add(board[i][j])
                    else:
                        gridMap[(i//3,j//3)] = set()
                        gridMap[(i//3,j//3)].add(board[i][j])
        return True

        