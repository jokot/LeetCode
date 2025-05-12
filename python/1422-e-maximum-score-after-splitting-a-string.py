# https://leetcode.com/problems/maximum-score-after-splitting-a-string
class Solution:
    def maxScore(self, s: str) -> int:
        result = 0

        for i in range(1, len(s)):
            result = max(result, s[:i].count('0') + s[i:].count('1'))
        
        return result

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("011101", 5),               # LeetCode example
        ("00111", 5),                # All zeros on left
        ("1111", 3),                 # All ones
        ("00", 1),                   # Minimum length string
        ("01", 2),                   # Simple case
        ("0000", 3),                # All zeros
        ("100", 1),                 # Three characters
        ("11000", 2),               # Mixed case
        ("11111110", 6),            # One zero at end
        ("00000001", 8),            # One one at end
    ]
    
    # Run tests
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.maxScore(s)
        print(f"Test {i}:")
        print(f"Input: '{s}'")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        