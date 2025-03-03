# https://leetcode.com/problems/reshape-the-matrix/

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        result = [[0] * c for _ in range(r)]

        for i in range(m * n):
            ori_row, ori_col = i // n, i % n

            res_row, res_col = i // c, i % c

            result[res_row][res_col] = mat[ori_row][ori_col]
        
        return result

def test_solution():
    solution = Solution()
    
    data = [[1,2],[3,4]]
    r=1
    c=4
    expected = [[1,2,3,4]]
    result = solution.matrixReshape(data, r, c)
    assert result == expected

    data = [[1,2],[3,4]]
    r=2
    c=4
    expected = [[1,2],[3,4]]
    result = solution.matrixReshape(data, r, c)
    assert result == expected

    print("All test case passed!")

if __name__ == '__main__':
    test_solution()