# https://leetcode.com/problems/find-pivot-index/description/
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        
        return -1

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (nums, expected_output)
    test_cases = [
        ([1,7,3,6,5,6], 3),           # LeetCode example 1
        ([1,2,3], -1),                # LeetCode example 2
        ([2,1,-1], 0),                # LeetCode example 3
        ([0], 0),                     # Single element zero
        ([1], 0),                    # Single non-zero element
        ([-1,-1,-1,0,1,1], 0),        # Negative numbers
        ([1,1,1,1], -1),              # All same numbers
        ([-1,-1,0,1,1,0], 5),         # Zero at end
        ([0,0,0], 0),                 # Multiple zeros
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.pivotIndex(nums)
        print(f"Test Case {i}:")
        print(f"Input array: {nums}")
        print(f"Expected pivot index: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)