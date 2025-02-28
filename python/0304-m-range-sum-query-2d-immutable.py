from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                total += self.matrix[i][j]
        
        return total

# Runner and test cases
def test_num_matrix():
    # Test case 1
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(2, 1, 4, 3) == 8
    assert num_matrix.sumRegion(1, 1, 2, 2) == 11
    assert num_matrix.sumRegion(1, 2, 2, 4) == 12

    # Test case 2
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(0, 0, 1, 1) == 12
    assert num_matrix.sumRegion(1, 1, 2, 2) == 28
    assert num_matrix.sumRegion(0, 0, 2, 2) == 45

    # Test case 3
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(0, 0, 2, 2) == 9
    assert num_matrix.sumRegion(1, 1, 2, 2) == 4
    assert num_matrix.sumRegion(0, 0, 1, 1) == 4

    # Test case 4
    matrix = [
        [2, 2],
        [2, 2]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(0, 0, 1, 1) == 8
    assert num_matrix.sumRegion(0, 0, 0, 0) == 2
    assert num_matrix.sumRegion(1, 1, 1, 1) == 2

    # Test case 5
    matrix = [
        [5]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(0, 0, 0, 0) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_num_matrix()