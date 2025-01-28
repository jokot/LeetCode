# https://leetcode.com/problems/baseball-game/
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for op in operations:
            if op == "C":
                points.pop()
            elif op == "D":
                points.append(points[-1] * 2)
            elif op == "+":
                points.append(points[-1] + points[-2])
            else:
                points.append(int(op))
        return sum(points)

# Runner code with sample input
if __name__ == "__main__":
    # Sample test cases
    test_cases = [
        ["5","2","C","D","+"],             # Expected output: 30
        ["5","-2","4","C","D","9","+","+"], # Expected output: 27
        ["1","C"],                          # Expected output: 0
    ]
    
    solution = Solution()
    
    # Test each case
    for ops in test_cases:
        result = solution.calPoints(ops)
        print(f"Operations: {ops}")
        print(f"Final score: {result}")
        print("-" * 50)
