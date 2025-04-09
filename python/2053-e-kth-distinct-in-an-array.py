# https://leetcode.com/problems/kth-distinct-string-in-an-array/
from collections import defaultdict
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = defaultdict(int)

        for a in arr:
            count[a] += 1

        for key, val in count.items():
            if k == 1 and val == 1:
                return key
            elif val == 1:
                k -= 1

        return ""

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["d","b","c","b","c","a"], 2, "a"),    # 2nd distinct is "a"
        (["aaa","aa","a"], 1, "aaa"),           # 1st distinct is "aaa"
        (["a","b","a"], 2, ""),                # 2nd distinct is "b"
        (["a","b","c"], 3, "c"),                # 3rd distinct is "c"
        (["a","a","a"], 1, ""),                 # No distinct strings
        (["a","b"], 3, ""),                     # k larger than distinct count
        ([], 1, ""),                            # Empty array
        (["x"], 1, "x"),                        # Single element
        (["a","b","c","d"], 1, "a"),           # All distinct
    ]
    
    # Run tests
    for i, (arr, k, expected) in enumerate(test_cases, 1):
        result = solution.kthDistinct(arr, k)
        print(f"Test {i}:")
        print(f"Input array: {arr}")
        print(f"k: {k}")
        print(f"Expected: '{expected}'")
        print(f"Result: '{result}'")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()