from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)
        
        return sum(max(row[j] for row in grid) for j in range(len(grid[0])))
        
# Runner and test cases
def test_delete_greatest_value():
    solution = Solution()

    # Test case 1
    grid = [
        [1, 2, 4],
        [3, 3, 1]
    ]
    expected = 8
    result = solution.deleteGreatestValue(grid)
    assert result == expected

    # Test case 2
    grid = [
        [10, 20, 30],
        [5, 15, 25],
        [1, 2, 3]
    ]
    expected = 60
    result = solution.deleteGreatestValue(grid)
    assert result == expected

    # Test case 3
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    expected = 3
    result = solution.deleteGreatestValue(grid)
    assert result == expected

    # Test case 4
    grid = [
        [5, 4, 3],
        [2, 1, 0]
    ]
    expected = 12
    result = solution.deleteGreatestValue(grid)
    assert result == expected

    # Test case 5
    grid = [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3]
    ]
    expected = 24
    result = solution.deleteGreatestValue(grid)
    assert result == expected

    print("All test cases passed!")

if __name__ == "__main__":
    test_delete_greatest_value()
