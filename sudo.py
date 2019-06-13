class Solution:
    def isValidSudoku(self, board) -> bool:
        # 每行的元素以一个字典储存，key是数字，value统一为1.
        dic_row = [[], [], [], [], [], [], [], [], []]
        dic_col = [[], [], [], [], [], [], [], [], []]
        dic_box = [[], [], [], [], [], [], [], [], []]

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3*(i//3)+(j//3)]:
                    dic_row[i].append(num)
                    dic_col[j].append(num)
                    # 利用地板除，向下取余。巧妙地将矩阵划分为九块
                    dic_box[3*(i//3)+(j//3)].append(num)
                else:
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
sol.isValidSudoku(para)
result = sol.isValidSudoku(para)
print(result)

arrar = [5, 6, 7, 8]
if 3 in arrar:
    print("is in ")
