from typing import List

# https://leetcode.com/problems/available-captures-for-rook/description/
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_row = 0
        rook_col = 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_row = i
                    rook_col = j
                    break
        count = 0

        # left
        for n in board[rook_row][:rook_col][::-1]:
            if n == 'p':
                count += 1
                break
            elif n == 'B':
                break
        
        # right
        for n in board[rook_row][rook_col+1:]:
            if n == "p":
                count += 1
                break
            elif n == "B":
                break

        # top
        for i in range(rook_row-1, -1, -1):
            if board[i][rook_col] == "p":
                count += 1
                break
            elif board[i][rook_col] == "B":
                break
        
        # bottom
        for i in range(rook_row+1, 8):
            if board[i][rook_col] == "p":
                count += 1
                break
            elif board[i][rook_col] == "B":
                break

        return count

# Runner and test cases
def test_num_rook_captures():
    solution = Solution()

    # Test case 1
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
    expected = 3
    result = solution.numRookCaptures(board)
    assert result == expected

    # Test case 2
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", "p", "p", "p", "p", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."],
        [".", "p", "B", "R", "B", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."],
        [".", "p", "p", "p", "p", "p", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
    expected = 0
    result = solution.numRookCaptures(board)
    assert result == expected

    # Test case 3
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        ["p", "p", ".", "R", ".", "p", "B", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
    expected = 3
    result = solution.numRookCaptures(board)
    assert result == expected

    # Test case 4
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
    expected = 0
    result = solution.numRookCaptures(board)
    assert result == expected

    # Test case 5
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
    expected = 0
    result = solution.numRookCaptures(board)
    assert result == expected

    print("All test cases passed!")

if __name__ == "__main__":
    test_num_rook_captures()
