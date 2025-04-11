# https://leetcode.com/problems/find-missing-and-repeated-values/
from collections import defaultdict
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = defaultdict(int)
        result = [0,0]

        for row in grid:
            for v in row:
                seen[v] += 1
        
        for i in range(1, n*n+1):
            if seen[i] > 1:
                result[0] = i
            elif seen.get(i, 0) == 0:
                result[1] = i

        return result

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([[1,3],[3,2]], [3,4]),                           # 2x2 grid
        ([[9,1,7],[8,9,2],[3,4,6]], [9,5]),              # 3x3 grid
        ([[1,1],[2,3]], [1,4]),                          # 2x2 with repeat at corner
        ([[1,2],[2,4]], [2,3]),                          # 2x2 with repeat in middle
        ([[1,2,3],[4,5,6],[7,7,9]], [7,8]),             # 3x3 with repeat in last row
        ([[1,2,2],[3,4,5],[6,7,8]], [2,9]),             # 3x3 with repeat in first row
    ]
    
    # Run tests
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = solution.findMissingAndRepeatedValues(grid)
        print(f"Test {i}:")
        print(f"Input grid:")
        for row in grid:
            print(f"  {row}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()