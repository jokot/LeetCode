# https://leetcode.com/problems/longest-palindrome/
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        isOddExist = False
        result = 0
        for val in counter.values():
            if val > 1:
                if val % 2 == 0:
                    result += val
                else:
                    isOddExist = True
                    result += val - 1
            else:
                isOddExist = True
        if isOddExist:
            result += 1
        return result

def main():
    # Test cases: (input_string, expected_output)
    test_cases = [
        ("abccccdd", 7),               # LeetCode example 1
        ("a", 1),                      # Single character
        ("", 0),                       # Empty string
        ("aaa", 3),                    # All same characters
        ("abc", 1),                    # No pairs
        ("aabbccddee", 10),           # All pairs
        ("aabbccddeeee", 12),         # Multiple pairs with extras
        ("zzzzzzzz", 8),              # Even count of same character
        ("zzzzzzz", 7),               # Odd count of same character
        ("aAbB", 1),                  # Case sensitive pairs
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.longestPalindrome(s)
        print(f"Test Case {i}:")
        print(f"Input: {s}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)

if __name__ == "__main__":
    main()
