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
        lineResult = [('.' * j + 'Q' + '.' * (n-j - 1))
                      for i in result for j in i]
        lastPrintStr = [lineResult[l:l+n]
                        for l in range(0, len(lineResult), n)]
        print(lastPrintStr)
        return lastPrintStr


testResult = Solution()
# testResult.solveNQueens(4)


class Solution2:

    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.dfs(0, 0, 0, 0, n)
        return self.count

    def dfs(self, row, col, pie, na, n):
        if(row >= n):
            self.count += 1
            return
        # """ 获取可以放置的所在位, col, pie, na的二进制上的1表示已会被攻击的位置，不能放置
        # 另外要获取前n（n皇后）的为位数，超出去就没用了 """
        placeBits = (~(col | pie | na)) & ((1 << n) - 1)
        # > 0表示有可以使用的位数
        while placeBits > 0:
            # 取出最右边的1的位置的对应值，相当于是占据了
            placeV = placeBits & -placeBits
            self.dfs(row+1, col | placeV, (pie | placeV)
                     << 1, (na | placeV) >> 1, n)
            placeBits = placeBits & (placeBits - 1)


solution2 = Solution2()
print(solution2.totalNQueens(4))
