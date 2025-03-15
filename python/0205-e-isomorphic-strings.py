class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s,t):
            if (cs in s_to_t and s_to_t[cs] != ct) or (ct in t_to_s and t_to_s[ct] != cs):
                return False
            else:
                s_to_t[cs] = ct
                t_to_s[ct] = cs
            
        return True

def test_isomorphic_strings():
    solution = Solution()
    
    # Test cases as (s, t, expected_result)
    test_cases = [
        # Basic test cases
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        
        # The problematic test case
        ("egcd", "adfd", False),
        
        # Edge cases
        ("", "", True),
        ("a", "a", True),
        ("ab", "aa", False),
        
        # Different lengths
        ("abc", "ab", False),
        
        # Same character mapping to different characters
        ("badc", "baba", False),
        
        # Different characters mapping to same character
        ("abc", "aaa", False),
        
        # Complex cases
        ("abcdefghijklm", "nopqrstuvwxyz", True),
        ("aabbccdd", "qqwweeqq", False),
    ]
    
    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = solution.isIsomorphic(s, t)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Input: s = '{s}', t = '{t}'")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_isomorphic_strings()
    