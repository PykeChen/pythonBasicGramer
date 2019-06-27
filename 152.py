
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0] * 2 for index in range(2)]
        dp[0][0], dp[0][1] = nums[0], nums[0]
        res = nums[0]
        for tkey, value in enumerate(nums[1:]):
            tmpkey = tkey + 1
            key, otherK = tmpkey % 2, (tmpkey-1) % 2
            if value > 0:
                dp[key][0] = max(value * dp[otherK][0], value)
                dp[key][1] = min(value * dp[otherK][1], value)
            else:
                dp[key][0] = max(value * dp[otherK][1], value)
                dp[key][1] = min(value * dp[otherK][0], value)
            res = max(res, dp[key][0])
        return res


so = Solution()
print(so.maxProduct([2, 3, -2, 4]))
