# https://leetcode.com/problems/maximum-number-of-balloons/
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }

        ballonCount = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }
        
        count = 0
        wordCount = 7

        for c in text:
            charCount = ballonCount.get(c, -1)
            if  charCount > 0:
                ballonCount[c] = charCount - 1
                wordCount -= 1 
            
            if wordCount == 0:
                count += 1
                ballonCount = {
                    'b': 1,
                    'a': 1,
                    'l': 2,
                    'o': 2,
                    'n': 1
                }
                wordCount = 7

        return count

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (text, expected_output)
    test_cases = [
        ("nlaebolko", 1),                 # LeetCode example 1
        ("loonbalxballpoon", 2),          # LeetCode example 2
        ("leetcode", 0),                  # LeetCode example 3
        ("balloon", 1),                   # Single balloon
        ("balloonballoon", 2),            # Two complete balloons
        ("balon", 0),                     # Missing letters
        ("bballoonn", 1),                 # Extra letters but one balloon
        ("ballllllooooonn", 1),          # Multiple l and o but one balloon
        ("", 0),                          # Empty string
        ("balloonballoonballoon", 3),     # Three complete balloons
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (text, expected) in enumerate(test_cases, 1):
        result = solution.maxNumberOfBalloons(text)
        print(f"Test Case {i}:")
        print(f"Input text: '{text}'")
        print(f"Expected number of 'balloon': {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)
