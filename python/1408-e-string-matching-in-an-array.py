# https://leetcode.com/problems/string-matching-in-an-array/
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for i, val in enumerate(words):
            others = words[:i] + words[i+1:]
            for o in others:
                if val in o:
                    result.append(val)
                    break
        
        return result

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["mass","as","hero","superhero"], ["as","hero"]),
        (["leetcode","et","code"], ["et","code"]),
        (["blue","green","bu"], []),
        (["leetcoder","leetcode","od","hamlet"], ["leetcode","od"]),
        (["single"], []),                              # Single word
        (["cat", "dog"], []),                         # No substring matches
        (["tech","technology","detect"], ["tech"]),    # Multiple matches for same word
        (["mass"], []),                       # Duplicate words
    ]
    
    # Run tests
    for i, (words, expected) in enumerate(test_cases, 1):
        result = solution.stringMatching(words)
        # Sort both lists for consistent comparison
        result.sort()
        expected.sort()
        print(f"Test {i}:")
        print(f"Input: {words}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        