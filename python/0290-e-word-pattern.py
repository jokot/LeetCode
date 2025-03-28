# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        s_split = s.split()
        if len(pattern) != len(s_split) or len(set(pattern)) != len(set(s_split)):
            return False

        for (c, word) in zip(pattern, s_split):
            seen = mapping.get(c, "-")
            if seen == "-":
                mapping[c] = word
            else:
                if seen != word:
                    return False
        
        return True

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog dog dog dog", True),
        ("abba", "dog dog dog dog", False),
        ("abc", "dog cat dog", False),
    ]
    
    # Run tests
    for i, (pattern, s, expected) in enumerate(test_cases, 1):
        result = solution.wordPattern(pattern, s)
        print(f"Test {i}:")
        print(f"Pattern: {pattern}")
        print(f"String: {s}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()