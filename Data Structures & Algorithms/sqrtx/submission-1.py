class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            val = mid * mid

            if val == x:
                return mid
            elif val < x:
                left = mid + 1
            else:
                right = mid - 1

        return right