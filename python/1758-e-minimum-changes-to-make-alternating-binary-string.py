# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
class Solution:
    def minOperations(self, s: str) -> int:
        countEven = 0
        countOdd = 0
        for i in range(len(s)):
            c = s[i]
            if i % 2 == 0:
                if c == '0':
                    countEven += 1
                else:
                    countOdd += 1
            else:
                if c == '1':
                    countEven += 1
                else:
                    countOdd += 1

        return min(countEven, countOdd)

# Test runner
if __name__ == "__main__":
    # Test cases: (s, expected_output)
    test_cases = [
        ("0100", 1),             # LeetCode example 1
        ("10", 0),               # LeetCode example 2
        ("1111", 2),             # LeetCode example 3
        ("", 0),                 # Empty string
        ("0", 0),                # Single character
        ("01", 0),               # Already alternating
        ("00", 1),               # Same characters
        ("000111", 2),           # Groups of same characters
        ("11111111", 4),         # All ones
        ("00000000", 4),         # All zeros
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.minOperations(s)
        print(f"Test Case {i}:")
        print(f"Input: {s}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)
