# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for i in range(1, rowIndex + 1):
            result.append(result[-1] * (rowIndex - i + 1) // i)
        return result

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (0, [1]),                     # First row
        (1, [1,1]),                   # Second row
        (2, [1,2,1]),                 # Third row
        (3, [1,3,3,1]),              # Fourth row
        (4, [1,4,6,4,1]),            # Fifth row
        (5, [1,5,10,10,5,1]),        # Sixth row
        (6, [1,6,15,20,15,6,1]),     # Seventh row
        (7, [1,7,21,35,35,21,7,1]),  # Eighth row
        (30, [1,30,435,4060,27405,142506,593775,2035800,5852925,14307150,30045015,54627300,86493225,119759850,145422675,155117520,145422675,119759850,86493225,54627300,30045015,14307150,5852925,2035800,593775,142506,27405,4060,435,30,1])  # Large row
    ]
    
    # Run tests
    for i, (rowIndex, expected) in enumerate(test_cases, 1):
        result = solution.getRow(rowIndex)
        print(f"Test {i}:")
        print(f"Row Index: {rowIndex}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        