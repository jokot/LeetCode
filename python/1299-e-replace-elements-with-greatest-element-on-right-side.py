# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        if len(arr) == 2:
            return [arr[1],-1]
        if len(arr) == 3:
            return [max(arr[1:]), arr[2], -1]
        
        prev = 0
        for i in range(len(arr) - 3, -1, -1):
            temp = arr[i]
            arr[i] = max(arr[i+1], arr[i+2], prev)
            prev = temp
        arr[-2] = arr[-1]
        arr[-1] = -1
        
        return arr

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (input_array, expected_output)
    test_cases = [
        ([17,18,5,4,6,1], [18,6,6,6,1,-1]),      # LeetCode example
        ([400], [-1]),                            # Single element
        ([1,2], [2,-1]),                         # Two elements
        ([1,2,3], [2,3,-1]),                     # Three elements
        ([10,9,8,7], [9,8,7,-1]),               # Decreasing array
        ([1,2,3,4,5], [5,5,5,5,-1]),            # Increasing array
        ([1,1,1,1], [1,1,1,-1])                 # Same elements
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (input_arr, expected) in enumerate(test_cases, 1):
        arr = input_arr.copy()  # Create a copy to preserve original input
        result = solution.replaceElements(arr)
        print(f"Test Case {i}:")
        print(f"Input array: {input_arr}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)