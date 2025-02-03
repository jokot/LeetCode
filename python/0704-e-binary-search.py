
# https://leetcode.com/problems/binary-search/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)//2, len(nums)-1)

    def binarySearch(self, nums: List[int], target: int, left: int, center: int, right: int) -> int:
        if (left > right):
            return -1
        
        if nums[center] == target:
            return center
        elif nums[center] > target:
            right = center - 1
            center = (left + right) // 2
            return self.binarySearch(nums, target, left, center, right)
        else: 
            left = center + 1
            center = (left + right) // 2
            return self.binarySearch(nums, target, left, center, right)

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (nums, target, expected_output)
    test_cases = [
        ([-1,0,3,5,9,12], 9, 4),      # Target exists in array
        ([-1,0,3,5,9,12], 2, -1),     # Target doesn't exist
        ([5], 5, 0),                   # Single element, target exists
        ([5], 0, -1),                  # Single element, target doesn't exist
        ([1, 2, 3, 4, 5], 3, 2),      # Target in middle
        ([1, 2], 2, 1),               # Two elements
        ([], 5, -1),                   # Empty array
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.search(nums, target)
        print(f"Test Case {i}:")
        print(f"Array: {nums}")
        print(f"Target: {target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)