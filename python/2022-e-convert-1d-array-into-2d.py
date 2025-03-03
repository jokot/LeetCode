# https://leetcode.com/problems/convert-1d-array-into-2d-array/
from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        result = [[0]*n for _ in range(m)]
        for i in range(len(original)):
            result[i // n][i % n] = original[i]

        return result

def test_solution():
    solution = Solution()

    data = [1,2,3,4]
    m = 2
    n = 2
    expected = [[1,2],[3,4]]
    result = solution.construct2DArray(data, m, n)
    assert result == expected

    data = [1,2,3]
    m = 1
    n = 3
    expected = [[1,2,3]]
    result = solution.construct2DArray(data, m, n)
    assert result == expected

    data = [1,2]
    m = 1
    n = 1
    expected = []
    result = solution.construct2DArray(data, m, n)
    assert result == expected

    print("All test data passed!")


if __name__ == '__main__':
    test_solution()
    