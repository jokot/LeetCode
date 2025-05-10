# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = 10000
        b = 10000
        c = 0
        d = 0
        for n in nums:
            if n <= a:
                b = a
                a = n
            elif n <= b:
                b = n
            
            if n >= d:
                c = d
                d = n
            elif n >= c:
                c = n

        return c*d - a*b

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([5,6,2,7,4], 34),           # Example from LeetCode
        ([4,2,5,9,7,4,8], 64),       # Larger array
        ([1,2,3,4], 10),             # Minimal length array
        ([10,10,10,10], 0),          # All same numbers
        ([1,1,2,2], 3),              # Pairs of same numbers
        ([1,2,100,99], 9898),        # Large difference
        ([3,3,3,4], 3),              # Three same numbers
        ([1,6,7,5,2,4,10,6], 68),    # Array with duplicates
        ([1000,1000,1,1], 999999),   # Edge case with large numbers
    ]
    
    # Run tests
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.maxProductDifference(nums)
        print(f"Test {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()