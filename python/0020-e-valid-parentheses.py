# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: 
            return False

        openings = [0 for _ in range(len(s))]
        current = -1

        for c in s:
            if self.isOpening(c):
                current += 1
                openings[current] = c
            else:
                if current > -1 and self.isMatch(openings[current], c):
                    current -= 1
                else:
                    return False
                    
        return current == -1
    
    def isOpening(self, c: str) -> bool:
        return c == "{" or c == "[" or c == "("

    def isMatch(self, open: str, close: str) -> bool:
        if close == "}": return open == "{"
        elif close == ")": return open == "("
        elif close == "]": return open == "["
        else: return False

# Runner code with sample input
if __name__ == "__main__":
    # Sample test cases
    test_cases = [
        "()",           # Expected: True
        "()[]{}",       # Expected: True
        "(]",           # Expected: False
        "([)]",         # Expected: False
        "{[]}",         # Expected: True
        "]",            # Expected: False
        "",             # Expected: False
        "(()",          # Expected: False
    ]
    
    solution = Solution()
    
    # Test each case
    for s in test_cases:
        result = solution.isValid(s)
        print(f"Input string: '{s}'")
        print(f"Is valid: {result}")
        print("-" * 50)
        