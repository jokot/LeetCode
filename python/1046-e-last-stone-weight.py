# https://leetcode.com/problems/last-stone-weight/
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        max_heap = [-num for num in stones]

        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            a = heapq.heappop(max_heap)
            b = heapq.heappop(max_heap)
            result = abs(a - b)
            heapq.heappush(max_heap, result * -1)
        return max_heap[0] * -1

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test data
    test_cases = [
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
        ([3, 7, 2], 2),
        ([10, 4, 2, 10], 2),
        ([1, 1, 1, 1], 0)
    ]
    
    for i, (stones, expected) in enumerate(test_cases):
        assert solution.lastStoneWeight(stones) == expected, f"Test case {i + 1} failed"
    
    print("All test cases passed!")
