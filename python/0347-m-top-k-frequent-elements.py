# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        top = []
        
        for n in n.most_common(k):
            top.append(n[0])

        return top

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (nums, k, expected_output)
    test_cases = [
        ([1,1,1,2,2,3], 2, [1,2]),           # Basic case
        ([1], 1, [1]),                        # Single element
        ([1,2], 2, [1,2]),                    # k equals array length
        ([1,1,1,2,2,2], 2, [1,2]),           # Equal frequencies
        ([1,2,3,1,2,1], 2, [1,2]),           # Multiple frequencies
        ([4,1,-1,2,-1,2,3], 2, [-1,2])       # Negative numbers
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = solution.topKFrequent(nums, k)
        print(f"Test Case {i}:")
        print(f"Input array: {nums}")
        print(f"k: {k}")
        print(f"Expected top {k} frequent elements: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if sorted(result) == sorted(expected) else '✗ Failed'}")
        print("-" * 50)
