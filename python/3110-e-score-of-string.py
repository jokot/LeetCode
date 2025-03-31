# https://leetcode.com/problems/score-of-a-string/
class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1):
            count += abs(ord(s[i])-ord(s[i+1]))

        return count

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("abcd", 3),           # Regular sequence
        ("aaa", 0),            # Same characters
        ("az", 25),            # Large difference
        ("zyxw", 3),           # Descending sequence
        ("a", 0),              # Single character
        ("zza", 25),           # Mixed differences
        ("hello", 13),         # Common word
        ("ABC", 2),            # Uppercase letters
    ]
    
    # Run tests
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.scoreOfString(s)
        print(f"Test {i}:")
        print(f"Input: '{s}'")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()