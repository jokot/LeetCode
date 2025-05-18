# https://leetcode.com/problems/path-crossing/
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = [(0,0)]

        for i in range(len(path)):
            coor = seen[-1]
            if path[i] == 'N':
                coor = (coor[0], coor[1]+1)
            elif path[i] == 'S':
                coor = (coor[0], coor[1]-1)
            elif path[i] == 'E':
                coor = (coor[0]+1, coor[1])
            else:
                coor = (coor[0]-1, coor[1])
            if coor in seen:
                return True
            seen.append(coor)
        return False

# Test runner
if __name__ == "__main__":
    # Test cases: (path, expected_output)
    test_cases = [
        ("NES", False),           # LeetCode example 1
        ("NESWW", True),          # LeetCode example 2
        ("N", False),             # Single step
        ("NESW", True),           # Complete square
        ("NNNN", False),          # Straight line
        ("NEWS", True),          # Box without crossing
        ("NEWSNEWS", True),       # Double box with crossing
        ("", False),              # Empty path
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (path, expected) in enumerate(test_cases, 1):
        result = solution.isPathCrossing(path)
        print(f"Test Case {i}:")
        print(f"Path: {path}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)
