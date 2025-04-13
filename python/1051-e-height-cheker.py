# https://leetcode.com/problems/height-checker
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        diff = 0
        for m, n in zip(heights, sorted(heights)):
            if m != n:
                diff += 1
        return diff

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,1,4,2,1,3], 3),              # Example from LeetCode
        ([5,1,2,3,4], 5),                # Completely reversed
        ([1,2,3,4,5], 0),                # Already sorted
        ([1], 0),                        # Single element
        ([2,2,2,2], 0),                  # All same numbers
        ([1,2,1,2,1], 2),                # Alternating pattern
        ([3,1,2,1], 2),                  # Small unsorted array
        ([], 0),                         # Empty array
        ([5,4,3,2,1], 4),               # Strictly decreasing
    ]
    
    # Run tests
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.heightChecker(heights)
        print(f"Test {i}:")
        print(f"Input heights: {heights}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        