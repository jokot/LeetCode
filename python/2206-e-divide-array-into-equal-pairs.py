# https://leetcode.com/problems/divide-array-into-equal-pairs/

from typing import List
from collections import defaultdict, Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for val in count.values():
            if val%2 != 0:
                return False

        return True

# Test runner
if __name__ == "__main__":
    # Test cases: (nums, expected_output)
    test_cases = [
        ([3,2,3,2,2,2], True),          # LeetCode example 1
        ([1,2,3,4], False),             # LeetCode example 2
        ([1,1], True),                  # Single pair
        ([1,1,2,2,3,3], True),         # Multiple different pairs
        ([1,1,1,1], True),             # Same number pairs
        ([1,2,3], False),              # Odd length
        ([1,1,2,3], False),            # Cannot form pairs
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.divideArray(nums)
        print(f"Test Case {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)

