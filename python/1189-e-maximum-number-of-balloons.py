# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        one = defaultdict(int)
        two = defaultdict(int)

        for c in text:
            if c == 'b' or c =='a' or c == 'n':
                one[c] += 1
            elif c == 'l' or c == 'o':
                two[c] += 1
                
        if one and two and len(one) == 3 and len(two) == 2:
            oneMin = min(list(one.values()))
            twoMin = min(list(two.values()))
            return min(oneMin, twoMin//2) 

        return 0

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
