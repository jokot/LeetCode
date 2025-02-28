from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.aux_matrix = self.calculate_aux_matrix(matrix)
    
    def calculate_aux_matrix(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        aux_matrix = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    aux_matrix[0][0] = matrix[0][0]
                elif i == 0:
                    aux_matrix[0][j] = aux_matrix[0][j-1]+matrix[0][j]
                elif j == 0:
                    aux_matrix[i][0] = aux_matrix[i-1][0]+matrix[i][0]
                else:
                    aux_matrix[i][j] = aux_matrix[i-1][j]+aux_matrix[i][j-1]+matrix[i][j]-aux_matrix[i-1][j-1]

        return aux_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        if row1 == 0 and col1 == 0:
            return self.aux_matrix[row2][col2]
        elif row1 == 0:
            return self.aux_matrix[row2][col2] - self.aux_matrix[row2][col1-1]
        elif col1 == 0:
            return self.aux_matrix[row2][col2] - self.aux_matrix[row1-1][col2]
        else:
            return self.aux_matrix[row2][col2] - self.aux_matrix[row1-1][col2] - self.aux_matrix[row2][col1-1] + self.aux_matrix[row1-1][col1-1]
    


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

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