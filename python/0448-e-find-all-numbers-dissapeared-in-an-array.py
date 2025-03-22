# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        nums_set = set(nums)

        for i in range(n):
            if i+1 not in nums_set:
                result.append(i+1)

        return result

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (nums, expected_output)
    test_cases = [
        ([4,3,2,7,8,2,3,1], [5,6]),           # LeetCode example
        ([1,1], [2]),                          # Duplicate numbers
        ([1,1,1,1], [2,3,4]),                 # Multiple same number
        ([1,2,3,4], []),                      # No missing numbers
        ([2,2], [1]),                         # All same numbers
        ([1], []),                            # Single element
        ([], []),                             # Empty array
        ([2,3,4,5,6,7,8,9], [1]),            # Missing first number
        ([1,2,3,4,5,6,7,8,8], [9]),            # Missing last number
        ([1,1,1,2,2,3,3,4], [5,6,7,8])       # Multiple missing numbers
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.findDisappearedNumbers(nums)
        print(f"Test Case {i}:")
        print(f"Input array: {nums}")
        print(f"Expected missing numbers: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)

        