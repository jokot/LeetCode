# https://leetcode.com/problems/reshape-the-matrix/

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        
        output = [[1]*c for _ in range(r)]
        
        R = 0
        C = 0
        for row in mat:
            for val in row:
                output[R][C] = val
                if C == c - 1:
                    C = 0
                    R += 1
                else:
                    C += 1
        return output

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