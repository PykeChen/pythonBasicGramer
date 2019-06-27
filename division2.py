import math


class Solution:

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 0, x
        mid = 0
        while (l < r):
            mid = (l + r) / 2
            if math.fabs(mid * mid - x) < 1e-10:
                break
            elif mid * mid < x:
                l = mid
            else:
                r = mid
        return mid


so = Solution()
print(f'{so.mySqrt(8):.4f}')
