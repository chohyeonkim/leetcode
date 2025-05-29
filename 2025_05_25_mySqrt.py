class Solution:
    def mySqrt(self, x: int) -> int:

        l = 1
        r = x

        while l <= r:

            m = (l + r) // 2

            squre_m = m * m

            if squre_m == x:
                return m

            if squre_m > x:
                r = m - 1

            else:
                l = m + 1

        return r
