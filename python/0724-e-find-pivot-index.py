# https://leetcode.com/problems/find-pivot-index/description/
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left_sum = []
        right_sum = []

        for i in range(len(nums)):
            right = len(nums)-i-1
            if i == 0:
                left_sum.append(nums[0])
                right_sum.append(nums[right])
            else:
                left_sum.append(nums[i] + left_sum[-1])
                right_sum.append(nums[right] + right_sum[-1])

        right_sum = right_sum[::-1]

        if not right_sum[1]:
            return 0

        for i in range(1, len(nums)-1):
            if left_sum[i-1] == right_sum[i+1]:
                return i

        if not left_sum[len(nums)-2]:
            return len(nums)-1

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