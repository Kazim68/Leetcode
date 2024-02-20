class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkBoxes(board)


    def checkRows(self, board):
        for row in board:
            bank = {}
            for cell in row:
                if cell != '.' and cell in bank: 
                    return False
                bank[cell] = 1
        return True

    def checkCols(self, board):
        for i in range(9):
            bank = {}
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in bank: return False
                bank[board[j][i]] = 1
        return True
    
    def checkBoxes(self, board):
        for box in range(9):
            row = (box // 3) * 3
            col = 3 * (box % 3)
            if not self.iterateBox(board, row, col): return False
        return True
            
    
    def iterateBox(self, board, row, col):
        bank = {}
        for i in range(3):
            for j in range(3):
                cell = board[row + i][col + j]
                if cell != '.' and cell in bank: return False
                bank[cell] = 1
        return True

