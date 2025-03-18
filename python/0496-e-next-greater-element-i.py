# https://leetcode.com/problems/next-greater-element-i
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) == 1:
            return [-1]

        nextGreater = {num: -1 for num in nums2}
        notSet = [nums2[0]]

        for i in range(1,len(nums2)):
            num = nums2[i]
            size = len(notSet)
            for j in range(size-1, -1, -1):
                ns = notSet[j]
                if ns < num:
                    nextGreater[ns] = num
                    notSet.pop()            
            notSet.append(num)
        
        return [nextGreater[num] for num in nums1]

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
