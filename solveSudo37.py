class Solution:

    def isValidAtPos(self, row, col, board):
        # 判断相同行是否有相同值
        valAtPos = board[row][col]
        for colVal in range(9):
            if colVal != col and board[row][colVal] == valAtPos:
                return False
        # 判断列
        for rowVal in range(9):
            if rowVal != row and board[rowVal][col] == valAtPos:
                return False
        # 判断3x3各自
        rowIndex = row // 3
        colIndex = col // 3
        for index in range(9):
            tmpRIndex = rowIndex * 3 + (index // 3)
            tmpCIndex = colIndex * 3 + (index % 3)
            if ((tmpRIndex != row or tmpCIndex != col) and
                    board[tmpRIndex][tmpCIndex] == valAtPos):
                return False
        return True

    def solveGenerator(self, row, col, board):
        print(f'row x col  = {row} x {col}', end='')
        if row == 9:
            return True
        print(f'row x col, value  = {board[row][col]}')
        if(board[row][col] == '.'):
            for value in range(1, 10, 1):
                board[row][col] = str(value)
                result = False
                if self.isValidAtPos(row, col, board):
                    if col == 8:
                        result = self.solveGenerator(row+1, 0, board)
                    else:
                        result = self.solveGenerator(row, col+1, board)
                    if result:
                        break
            if not result:
                board[row][col] = "."
            return result
        else:
            result = False
            if col == 8:
                result = self.solveGenerator(row+1, 0, board)
            else:
                result = self.solveGenerator(row, col+1, board)
            return result

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.solveGenerator(0, 0, board)


solution = Solution()
params = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solution.solveSudoku(params)
print(params)
