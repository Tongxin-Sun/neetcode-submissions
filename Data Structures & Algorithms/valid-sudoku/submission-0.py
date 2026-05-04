class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkColumn = [[] for _ in range(9)]
        checkSubBox = [[] for _ in range(9)]

        # Construct the column board
        for row in board:
            for i in range(9):
                checkColumn[i].append(row[i])

        #Construct the sub box board
        for i in range(9):
            for j in range(9):
                checkSubBox[i // 3 * 3 + j // 3].append(board[i][j])
        
        return self.checkDuplicates(board) and self.checkDuplicates(checkColumn) and self.checkDuplicates(checkSubBox)
    
    def checkDuplicates(self, board):
        for nums in board:
            nums_arr = []
            for num in nums:
                if num != ".":
                    if num in nums_arr:
                        return False
                    nums_arr.append(num)
        return True