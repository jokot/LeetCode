# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapGroup = defaultdict(list)

        for s in strs:
            key = self.createMapKey(s)
            mapGroup[key].append(s)
        
        return list(mapGroup.values())
            
    def createMapKey(self, str1):
        key = [0] * 26

        for c in str1:
            key[ord(c) - ord('a')] += 1
        
        return tuple(key)
    
# Runner and test cases
def test_group_anagrams():
    solution = Solution()

    # Test case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])

    # Test case 2
    strs = [""]
    expected = [[""]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])

    # Test case 3
    strs = ["a"]
    expected = [["a"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])

    # Test case 4
    strs = ["abc", "bca", "cab", "xyz", "zyx"]
    expected = [["abc", "bca", "cab"], ["xyz", "zyx"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])

    # Test case 5
    strs = ["abcd", "dcba", "bcda", "efgh", "hgfe"]
    expected = [["abcd", "dcba", "bcda"], ["efgh", "hgfe"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])

    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()