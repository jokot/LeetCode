# https://leetcode.com/problems/next-greater-element-i
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Process nums2 using stack - O(n) time
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Any remaining numbers in stack have no greater element
        for num in stack:
            next_greater[num] = -1
            
        # Map nums1 to their next greater elements - O(m) time
        return [next_greater[num] for num in nums1]

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (nums1, nums2, expected_output)
    test_cases = [
        ([4,1,2], [1,3,4,2], [-1,3,-1]),         # LeetCode example 1
        ([2,4], [1,2,3,4], [3,-1]),              # LeetCode example 2
        ([1], [1], [-1]),                         # Single element
        ([1,3,5,2,4], [6,5,4,3,2,1,7], [7,7,7,7,7]),  # Increasing at end
        ([1,2,3,4], [4,3,2,1], [-1,-1,-1,-1]),   # Decreasing array
        ([1,2], [2,1], [-1,-1]),                 # No greater elements
        ([1,2,3], [1,2,3], [2,3,-1]),           # Increasing array
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (nums1, nums2, expected) in enumerate(test_cases, 1):
        result = solution.nextGreaterElement(nums1, nums2)
        print(f"Test Case {i}:")
        print(f"nums1: {nums1}")
        print(f"nums2: {nums2}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)
