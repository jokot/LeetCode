# https://leetcode.com/problems/number-of-senior-citizens/
from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for s in details:
            if int(s[11:13]) > 60:
                count += 1
                
        return count

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["7868190130M7522", "5303914400F9211", "9273338290F4010"], 2),  # 2 seniors (75, 92)
        (["1313579440F2036", "2921522980M5644"], 0),                      # No seniors
        (["5612624052M6020"], 0),                                         # Age exactly 60
        (["1313579440F6136"], 1),                                         # One senior
        (["7868190130M6122", "5303914400F6211", "9273338290F6110"], 3),  # All seniors
        ([], 0),                                                          # Empty list
    ]
    
    # Run tests
    for i, (details, expected) in enumerate(test_cases, 1):
        result = solution.countSeniors(details)
        print(f"Test {i}:")
        print(f"Input: {details}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        