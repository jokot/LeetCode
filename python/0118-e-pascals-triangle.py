# https://leetcode.com/problems/pascals-triangle/
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        pascal_tri = [[1],[1,1]]
        for i in range(2, numRows):
            inner = [1]
            before = pascal_tri[i-1]
            for j in range(0, len(before)-1):
                inner.append(before[j] + before[j+1])
            inner.append(1)
            pascal_tri.append(inner)
        
        return pascal_tri

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (numRows, expected_output)
    test_cases = [
        (1, [[1]]),
        (2, [[1], [1,1]]),
        (3, [[1], [1,1], [1,2,1]]),
        (4, [[1], [1,1], [1,2,1], [1,3,3,1]]),
        (5, [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]), # Edge case
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (numRows, expected) in enumerate(test_cases, 1):
        result = solution.generate(numRows)
        print(f"Test Case {i}:")
        print(f"Number of rows: {numRows}")
        print(f"Expected triangle:")
        for row in expected:
            print(row)
        print(f"Got:")
        for row in result:
            print(row)
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)