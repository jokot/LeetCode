# https://leetcode.com/problems/string-matching-in-an-array/
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return []
        
        result = []

        for i in range(len(words)):
            for k in range(i+1, len(words)):
                if words[i] in words[k]:
                    result.append(words[i])
                elif words[k] in words[i]:
                    result.append(words[k])
        return list(set(result))

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
        