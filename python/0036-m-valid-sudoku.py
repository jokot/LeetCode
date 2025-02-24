from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkColumns(board) and self.checkBoxes(board)
    
    def checkRows(self, board):
        for row in board:
            empty = row.count(".")
            
            filled = len(set(row)) - int(not not empty)

            if empty + filled != len(row):
                return False
        return True

    def checkColumns(self, board):
        inverse_board = [[0 for i in range(9)] for j in range(9)]
        for i, row in enumerate(board):
            for j in range(len(row)):
                inverse_board[j][i] = board[i][j]
        
        return self.checkRows(inverse_board)
    
    def checkBoxes(self, board):
        group_board = [[0 for i in range(9)] for j in range(9)]
        X = 0
        J = 0
        for x in range(3):
            for y in range(3):
                J=0
                for i in range(3):
                    for j in range(3):
                        group_board[X][J] = board[3*x+i][3*y+j]
                        J += 1
                X += 1

        return self.checkRows(group_board)

# Runner and test cases
def test_is_valid_sudoku():
    solution = Solution()

    # Test case 1
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board) == True

    # Test case 2
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board) == False

    # Test case 3
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board) == True

    # Test case 4
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board) == True

    # Test case 5
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board) == True

    print("All test cases passed!")

if __name__ == "__main__":
    test_is_valid_sudoku()
