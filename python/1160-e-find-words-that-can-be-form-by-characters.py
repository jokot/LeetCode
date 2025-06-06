# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
from typing import List
from collections import defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        countChars = [0 for i in range(26)]

        for c in chars:
            countChars[ord(c) - ord('a')] += 1

        def isCanForm(word):
            chars = countChars.copy()
            for c in word:
                index = ord(c) - ord('a')
                if chars[index] == 0:
                    return False
                chars[index] -= 1
            
            return True
        
        count = 0

        for word in words:
            isCan = isCanForm(word)
            if isCan:
                count += len(word)

        return count

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["cat","bt","hat","tree"], "atach", 6),           # "cat" and "hat" can be formed
        (["hello","world","leetcode"], "welldonehoneyr", 10), # "hello" and "world" can be formed
        (["a"], "a", 1),                                   # Single character word and chars
        (["aa"], "a", 0),                                  # Not enough characters
        (["word"], "world", 4),                            # Single word that can be formed
        (["none"], "xyz", 0),                              # No words can be formed
        (["good","bad","test"], "goodbad", 7),            # Multiple words can be formed
        (["", "test"], "test", 4),                        # Empty string in words
        (["aaa","bbb"], "aaabbb", 6),                     # Multiple words with repeated chars
    ]
    
    # Run tests
    for i, (words, chars, expected) in enumerate(test_cases, 1):
        result = solution.countCharacters(words, chars)
        print(f"Test {i}:")
        print(f"Words: {words}")
        print(f"Characters: {chars}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()