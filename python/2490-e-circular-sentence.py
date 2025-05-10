# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        size = len(words)

        if words[0][0] != words[size-1][len(words[size-1])-1]:
            return False

        for i in range(size-1):
            first = words[i]
            second = words[i+1]

            if first[len(first)-1] != second[0]:
                return False
            
        return True

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("leetcode exercises sound delightful", True),     # First 'l', last 'l'
        ("eetcode", True),                                 # Single word, first 'e', last 'e'
        ("Leetcode is cool", False),                       # Not circular
        ("hello world", False),                            # Two words, not circular
        ("take me to semynak", False),                     # Multiple words, not circular
        ("happy new year", False),                         # Multiple words, not circular
        ("I love leetcode", False),                        # Multiple words, not circular
        ("general speak great enforce", True),             # Circular sentence
        ("gfg", True),                                     # Single word, circular
        ("a a", True),                                     # Two same words
        ("aaa bbb", False),                                # Two words, not circular
        ("cold ice cream", False),                         # Three words, not circular
    ]
    
    # Run tests
    for i, (sentence, expected) in enumerate(test_cases, 1):
        result = solution.isCircularSentence(sentence)
        print(f"Test {i}:")
        print(f"Input: '{sentence}'")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        