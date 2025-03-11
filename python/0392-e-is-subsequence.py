# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        if len(s) == len(t):
            if s == t:
                return True
            else:
                return False
        
        index = 0
        for i in range(len(t)):
            if index == len(s):
                return True
            if s[index] == t[i]:
                index += 1
            
        return index == len(s)

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (s, t, expected_output)
    test_cases = [
        ("abc", "ahbgdc", True),           # LeetCode example 1
        ("axc", "ahbgdc", False),          # LeetCode example 2
        ("", "ahbgdc", True),              # Empty s
        ("abc", "", False),                # Empty t
        ("abc", "abc", True),              # Equal strings
        ("abc", "ab", False),              # t shorter than s
        ("aaaaaa", "bbaaaa", False),       # Multiple same characters
        ("b", "abc", True),                # Single character subsequence
        ("abc", "abcde", True),            # s is prefix of t
        ("ace", "abcde", True),            # Scattered subsequence
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = solution.isSubsequence(s, t)
        print(f"Test Case {i}:")
        print(f"s: '{s}'")
        print(f"t: '{t}'")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)