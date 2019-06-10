class Solution:

    def solveNQueens(self, n: int):
        self.reuslt = []
        self.col, self.pie, self.na = set(), set(), set()
        self.traversal(n, 0, [])
        return self.genResult(n, self.reuslt)

    def traversal(self, n, row, resultStr):
        if row == n:
            self.reuslt.append(resultStr)
        for col in range(n):
            if (col not in self.col and (row + col) not in self.pie
                    and (row - col) not in self.na):
                self.col.add(col)
                self.pie.add(row + col)
                self.na.add(row - col)
                self.traversal(n, row+1, resultStr + [col])
                self.col.remove(col)
                self.pie.remove(row + col)
                self.na.remove(row - col)

    def genResult(self, n, result):
        lineResult = [('.' * j + 'Q' + '.' * (n-j - 1)) for i in result for j in i]
        lastPrintStr = [lineResult[l:l+n] for l in range(0, len(lineResult), n)]
        print(lastPrintStr)
        return lastPrintStr


testResult = Solution()
testResult.solveNQueens(4)
