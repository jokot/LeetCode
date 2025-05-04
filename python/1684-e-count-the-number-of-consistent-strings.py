# https://leetcode.com/problems/count-the-number-of-consistent-strings/
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            if set(word).issubset(set(allowed)):
                count += 1

        return count

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("ab", ["ad","bd","aaab","baa","badab"], 2),      # Only "aaab" and "baa" are consistent
        ("abc", ["a","b","c","ab","ac","bc","abc"], 7),   # All words are consistent
        ("cad", ["cc","acd","b","ba","bac","bad","ac","d"], 4),  # "cc","acd","ac","d" are consistent
        ("xyz", ["abc","def","ghi"], 0),                  # No consistent strings
        ("a", ["a","aa","aaa"], 3),                       # All strings with single character
        ("", [""], 1),                                    # Empty string case
        ("abcde", ["abcde"], 1),                          # Single word equal to allowed
        ("xy", ["xyz"], 0),                               # Word contains non-allowed character
        ("aeiou", ["aei","iou","aeio","aeiou","aio"], 5) # Vowels only
    ]
    
    # Run tests
    for i, (allowed, words, expected) in enumerate(test_cases, 1):
        result = solution.countConsistentStrings(allowed, words)
        print(f"Test {i}:")
        print(f"Allowed: '{allowed}'")
        print(f"Words: {words}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        