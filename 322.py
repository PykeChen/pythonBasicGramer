class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 表示集齐amount数量的钱币需要的最少货币是多少
        # dp[i] = dp[i - a[j]] + 1  j的范围是amount的
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1, 1):
            for c in coins:
                if(c <= i):
                    dp[i] = min(dp[i], dp[i-c] + 1)
        if dp[amount] > amount:
            return -1
        return dp[amount]


so = Solution()
print(so.coinChange([2], 3))
