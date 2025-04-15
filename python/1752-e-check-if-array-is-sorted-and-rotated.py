# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        index = 0

        current = 0
        for i, n in enumerate(nums):
            if current > n:
                index = i
                break
            current = n
        
        current = 0
        for n in nums[index:]+nums[:index]:
            if current > n:
                return False
            current = n

        return True

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([3,4,5,1,2], True),         # Rotated sorted array
        ([2,1,3,4], False),          # Not possible through rotation
        ([1,2,3], True),             # Already sorted
        ([1,1,1], True),             # All elements same
        ([2,1], True),               # Two elements, rotated
        ([1], True),                 # Single element
        ([6,7,1,2,3,4,5], True),     # Rotated at position 2
        ([3,3,4,1], True),           # Rotated at position 3
        ([5,4,3,2,1], False),        # Descending order
    ]
    
    # Run tests
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.check(nums)
        print(f"Test {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        