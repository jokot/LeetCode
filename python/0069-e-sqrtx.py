# https://leetcode.com/problems/sqrtx
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left = 1
        right = x

        while left <= right:
            mid = left + (right - left) // 2
            times = mid * mid
            if times == x:
                return mid
            elif times > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return left - 1
