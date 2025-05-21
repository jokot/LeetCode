from collections import defaultdict
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1: 
            return True

        all_count = defaultdict(int)

        for word in words:
            for c in word:
                all_count[c] += 1

        return len(set(all_count.values())) == 1 and sum(all_count.values()) > len(all_count)

def main():
    # Test cases
    solution = Solution()
    
    # Test case 1: Should return True
    test1 = ["abc", "aabc", "bc"]
    print(f"Test case 1: {test1}")
    print(f"Expected: True")
    print(f"Output: {solution.makeEqual(test1)}\n")
    
    # Test case 2: Should return False
    test2 = ["ab", "a"]
    print(f"Test case 2: {test2}")
    print(f"Expected: False")
    print(f"Output: {solution.makeEqual(test2)}\n")
    
    # Test case 3: Should return True
    test3 = ["caaaaa","aaaaaaaaa","aaaaaa","aaaaaaa","aaaaa","aaa","aaaa","a"]
    print(f"Test case 3: {test3}")
    print(f"Expected: True")
    print(f"Output: {solution.makeEqual(test3)}\n")

if __name__ == "__main__":
    main()