#


class Solution:

    def isValidAtPos(self, row, col, board):
        # 判断相同行是否有相同值
        valAtPos = board[row][col]
        for colVal in range(col+1, 9, 1):
            if board[row][colVal] == valAtPos:
                return False
        # 判断列
        for rowVal in range(row+1, 9, 1):
            if board[rowVal][col] == valAtPos:
                return False
        # 判断3x3各自
        rowIndex = int(row / 3)
        colIndex = int(col / 3)
        for index in range(9):
            tmpRIndex = rowIndex * 3 + int(index / 3)
            tmpCIndex = colIndex * 3 + (index % 3)
            if (tmpRIndex != row or tmpCIndex != col) and board[tmpRIndex][tmpCIndex] == valAtPos:
                return False
        return True

    def isValidSudoku(self, board) -> bool:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != ".":
                    valid = self.isValidAtPos(row, col, board)
                    if not valid:
                        return False

        return True


sol = Solution()
para = ([["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
result = sol.isValidSudoku(para)
print(result)
