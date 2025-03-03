# https://leetcode.com/problems/matrix-cells-in-distance-order/
from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[i // cols, i % cols] for i in range(rows * cols)], key = lambda val: self.count_distances(val[0], val[1], rCenter, cCenter))

    
    def count_distances(self, r1, c1, r2, c2):
        return abs(r1 - r2) + abs(c1 - c2)

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

    print("All test data passed!")

if __name__ == '__main__':
    test_solution()