# https://leetcode.com/problems/destination-city/
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = []
        end = []

        for path in paths:
            start.append(path[0])
            end.append(path[1])
        
        for e in end:
            if e not in start:
                return e

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]], "Sao Paulo"),
        ([["B","C"],["D","B"],["C","A"]], "A"),
        ([["A","Z"]], "Z"),
        ([["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]], "wxAscRuzOl"),
        ([["New York","Boston"],["Boston","Chicago"],["Chicago","Los Angeles"]], "Los Angeles"),
        ([["A","B"],["B","C"],["C","D"],["D","E"]], "E"),
        ([["X","Y"]], "Y"),
        ([["Tokyo","Seoul"],["Seoul","Beijing"],["Beijing","Shanghai"]], "Shanghai")
    ]
    
    # Run tests
    for i, (paths, expected) in enumerate(test_cases, 1):
        result = solution.destCity(paths)
        print(f"Test {i}:")
        print(f"Paths: {paths}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()