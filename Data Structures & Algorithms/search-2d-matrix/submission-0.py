class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        rL = 0 
        rR = row - 1
        def search(rowIndex,left, right):
            print("Inside search")
            if target < matrix[rowIndex][left] :
                print("moveUp")
                return "moveUp"
            elif target > matrix[rowIndex][right]:
                print("moveDown")
                return "moveDown"
            else:
                while left <= right :
                    middleR = (left+ right)//2
                    if matrix[rowIndex][middleR] == target:
                        print("INside")
                        return True
                    elif matrix[rowIndex][middleR]< target:
                        left = middleR+1
                    else:
                        right = middleR-1
                return False
        
        while(rL <= rR):
            print(rL,rR)
            middleRow = (rL + rR)//2
            result = search(middleRow, 0, column-1)
            if result == "moveUp" :
                rR = middleRow - 1
            elif result == "moveDown":
                rL = middleRow + 1
            else :
                return result
        return False


        
            
