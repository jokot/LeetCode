# https://leetcode.com/problems/number-of-good-pairs/
from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        count = 0
        for c in counts.values():
            count += (c*(c-1))//2
        
        return count

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,2,3,1,1,3], 4),          # Multiple pairs
        ([1,1,1,1], 6),              # All same numbers
        ([1,2,3], 0),                # No pairs
        ([1,2,3,1,1,3,3], 6),        # Multiple numbers with multiple pairs
        ([], 0),                      # Empty array
        ([5], 0),                     # Single element
        ([1,1], 1),                   # One pair
    ]
    
    # Run tests
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.numIdenticalPairs(nums)
        print(f"Test {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        