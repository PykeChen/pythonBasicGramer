class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # pt[index][k][0] 表示第index天， 最多进行k比交易，手上持没有持有股票的最大收益，
        # pt[index][k][1] 表示第index天， 最多进行k比交易，手上持持有一个股票的最大收益
        pt = [[[0 for _ in range(2)] for _ in range(k+1)] for i in prices]
        for index in range(0, len(prices)):
            for kp in range(k+1):
                if kp == 0:
                    # base class
                    pt[index][0][0] = 0
                    pt[index][0][1] = -float('inf')
                elif index == 0:
                    pt[index][kp][0] = 0
                    pt[index][kp][1] = -prices[0]
                else:
                    pt[index][kp][0] = max(
                        pt[index-1][kp][0], (pt[index-1][kp][1] + prices[index]))
                    pt[index][kp][1] = max(
                        pt[index-1][kp][1], (pt[index-1][kp-1][0] - prices[index]))

        return pt[len(prices)-1][k][0]


so = Solution()
print(so.maxProfit(2, [3, 2, 6, 5, 0, 3]))
