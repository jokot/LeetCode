# https://leetcode.com/problems/matrix-cells-in-distance-order/
from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        max_distance = rows + cols
        buckets = [[] for _ in range(max_distance)]

        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                buckets[distance].append([r,c])
        
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result

def test_solution():
    solution = Solution()

    rows = 1
    cols = 2
    rCenter = 0
    cCenter = 0
    expected = [[0,0],[0,1]]
    result = solution.allCellsDistOrder(rows, cols, rCenter, cCenter)
    assert result == expected

    rows = 2
    cols = 2
    rCenter = 0
    cCenter = 1
    expected = [[0,1],[0,0],[1,1],[1,0]]
    result = solution.allCellsDistOrder(rows, cols, rCenter, cCenter)
    assert result == expected

    rows = 2
    cols = 3
    rCenter = 1
    cCenter = 2
    expected = [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
    result = solution.allCellsDistOrder(rows, cols, rCenter, cCenter)
    assert result == expected 

    print("All test data passed!")

if __name__ == '__main__':
    test_solution()