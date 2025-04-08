# https://leetcode.com/problems/maximum-ascending-subarray-sum/
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = nums[0]
        inc = nums[0]

        for i in range(1, len(nums)):
            delta = nums[i] - nums[i-1]
            if delta > 0:
                inc += nums[i]
            else:
                inc = nums[i]
            
            result = max(inc, result)
        
        return result

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (nums, expected_output)
    test_cases = [
        ([10,20,30,5,10,50], 65),         # LeetCode example 1
        ([10,20,30,40,50], 150),          # LeetCode example 2
        ([12,17,15,13,10,11,12], 33),     # LeetCode example 3
        ([1], 1),                         # Single element
        ([5,4,3,2,1], 5),                # Descending array
        ([1,1,1,1], 1),                  # Equal elements
        ([3,6,10,1,8,9,3], 19),          # Multiple ascending subarrays
        ([1,2,3,4,5], 15),               # Strictly ascending
        ([100,1,2,3,4], 100)             # Large first element
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.maxAscendingSum(nums)
        print(f"Test Case {i}:")
        print(f"Input array: {nums}")
        print(f"Expected maximum ascending sum: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)