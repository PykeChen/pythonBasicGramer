class Solution:

    def gen(self, leftUsed: int, rightUsed: int, n: int, result, list):
        """ 迭代函数s
            @param leftUsed 已用的数量 
            @param rightUsed 已经用数量
        """
        if n < 0:
            return ""
        if leftUsed < n:
            self.gen(leftUsed + 1, rightUsed, n, result + "(", list)
        if rightUsed < leftUsed and rightUsed < n:
            self.gen(leftUsed, rightUsed + 1, n, result + ")", list)            
        if leftUsed == n and rightUsed == n:
            list.append(result)

    def generateParenthesis(self, n: int):

        self.gen(0, 0, n, "", list)
        return list


so = Solution()
list = so.generateParenthesis(2)
print(list)
