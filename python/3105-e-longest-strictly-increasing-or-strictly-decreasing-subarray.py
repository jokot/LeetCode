# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = 1
        decrease = 1
        max_len = 1

        for i in range(len(nums)-1):
            delta = nums[i+1]-nums[i]
            if delta > 0:
                increase += 1
                decrease = 1
            elif delta < 0 :
                decrease += 1
                increase = 1
            else:
                increase = 1
                decrease = 1
            
            max_len = max(max_len, increase, decrease)
        
        print(max_len, increase, decrease)

        return max_len

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([8,4,3,2,6,4,3], 4),         # Decreasing sequence: 8,4,3,2
        ([1,2,3,4,5], 5),             # Strictly increasing
        ([5,4,3,2,1], 5),             # Strictly decreasing
        ([1], 1),                      # Single element
        ([1,1,1], 1),                  # All equal
        ([1,2,2,3], 2),               # With equal elements
        ([1,2,1,2,1], 2),             # Alternating
        ([4,5,3,2,6], 3),             # Mixed pattern
        ([1,2,3,2,1], 3),             # Mountain pattern
    ]
    
    # Run tests
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.longestMonotonicSubarray(nums)
        print(f"\nTest {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
