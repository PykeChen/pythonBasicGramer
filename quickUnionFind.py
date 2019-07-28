class UnitFind:

    def __init__(self, grids):
        row = len(grids)
        col = len(grids[0])
        self.roots = [i * row + j for i in range(row) for j in range(col)]
        self.rank = [0] * (row * col)
        self.count = 0
        for i in range(row):
            for j in range(col):
                if grids[i][j] == '1':
                    self.roots[i * col + j] = i * col + j
                    self.count += 1

    def findRoot(self, i):
        root = i
        while self.roots[root] != root:
            root = self.roots[root]
        # 重新排列这个i的父序列，重拍，减小直接到root的层级
        while self.roots[i] != i:
            temp = self.roots[i]
            self.roots[i] = root
            i = temp
        return root

    def union(self, p, q):
        rootP = self.findRoot(p)
        rootQ = self.findRoot(q)
        if rootP != rootQ:
            if self.rank[rootP] < self.rank[rootQ]:
                self.roots[rootP] = rootQ
            elif self.rank[rootP] > self.rank[rootQ]:
                self.roots[rootQ] = rootP
            else:
                self.roots[rootQ] = rootP
                self.rank[rootP] += 1
            self.count -= 1


class Solution(object):
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        quickU = UnitFind(grid)
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                for dir in self.dirs:
                    nr, nc = i + dir[0], j + dir[1]
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                        quickU.union(i * col + j, nr * col + nc)
        return quickU.count