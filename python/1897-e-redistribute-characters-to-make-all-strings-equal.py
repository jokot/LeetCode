from collections import Counter
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        
        for val in Counter("".join(words)).values():
            if val % n != 0:
                return False
        return True

def main():
    # Test cases: (words, expected_output)
    test_cases = [
        (["abc", "aabc", "bc"], True),           # LeetCode example 1
        (["ab", "a"], False),                      # LeetCode example 2
        (["caaaaa","aaaaaaaaa","aaaaaa","aaaaaaa","aaaaa","aaa","aaaa","a"], False),  # LeetCode example 3
        ([], True),                               # Empty array
        (["a"], True),                            # Single string
        (["a", "a"], True),                       # Same strings
        (["abc", "def"], False),                  # Different characters
        (["aaa", "bbb", "ccc"], True),           # No common characters
        (["xy", "xy"], True),                     # Already equal
        (["a", "b", "c", "a", "b", "c"], False),   # Multiple equal distributions
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (words, expected) in enumerate(test_cases, 1):
        result = solution.makeEqual(words)
        print(f"Test Case {i}:")
        print(f"Input: {words}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)

if __name__ == "__main__":
    main()