class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            numSet = set()
            for j in range(9):
                if board[i][j] in numSet:
                    print('debug')
                    return False
                if board[i][j].isdigit():
                    numSet.add(board[i][j])
        
        for j in range(9):
            numSet = set()
            for i in range(9):
                if board[i][j] in numSet:
                    return False
                if board[i][j].isdigit():
                    numSet.add(board[i][j])
        
        for m in range(3):
            for k in range(3):
                numSet = set()
                for i in range(3):
                    for j in range(3):
                        if board[i + 3 * m][j + 3 * k] in numSet:
                            return False
                        if board[i + 3 * m][j + 3 * k].isdigit():
                            numSet.add(board[i + 3 * m][j + 3 * k])
        
        return True