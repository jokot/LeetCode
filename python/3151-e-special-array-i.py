# https://leetcode.com/problems/special-array-i/
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            nums[i] = nums[i] % 2 == 0
        
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return False

        return True

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,2,3], True),              # Alternating odd-even-odd
        ([2,2,3], False),             # Two consecutive even numbers
        ([1,1,2], False),             # Two consecutive odd numbers
        ([4,5], True),                # Even-odd pair
        ([1], True),                  # Single number
        ([2,3,4,5], True),            # Alternating even-odd sequence
        ([1,3,5,7], False),           # All odd numbers
        ([2,4,6,8], False),           # All even numbers
        ([1,2,3,4,5], True),          # Longer alternating sequence
    ]
    
    # Run tests
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Create a copy to preserve original input for display
        nums_copy = nums.copy()
        result = solution.isArraySpecial(nums_copy)
        print(f"Test {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()