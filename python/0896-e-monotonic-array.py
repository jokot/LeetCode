from typing import List
# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        increased = True
        current = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < current:
                increased = False
                break
            current = nums[i]

        decreased = True
        current = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > current:
                decreased = False
                break
            current = nums[i]

        return increased or decreased

# Test runner
if __name__ == "__main__":
    from typing import List
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,2,2,3], True),        # Increasing
        ([6,5,4,4], True),        # Decreasing
        ([1,3,2], False),         # Not monotonic
        ([1,2,4,5], True),        # Strictly increasing
        ([1,1,1], True),          # All equal
        ([1], True),              # Single element
        ([1,2,2,2,3], True),      # Non-strictly increasing
        ([3,2,1,1], True),        # Non-strictly decreasing
        ([2,2,2,1,4,5], False)    # Neither increasing nor decreasing
    ]
    
    # Run tests
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.isMonotonic(nums)
        print(f"Test {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()