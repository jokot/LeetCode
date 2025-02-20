# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create function is anagram
        #     input two string

        # create group anagram
        # add first item to first group
        # from index 1 to last index
        #     do check is anagram with input form current string and first item form first group
        #     if anagram then add it to the first group
        #     else move to the next group
        #         if next group empty
        #             create new grop
        #         else do the same checking (recursively / iteratively)

        group_anagrams = [[strs[0]]]

        for i in range(1, len(strs)):
            index, isAnagramOfGroups = self.isAnagramOfGroups(group_anagrams, strs[i])
            if isAnagramOfGroups:
                group_anagrams[index].append(strs[i])
            else:
                group_anagrams.append([strs[i]])
        return group_anagrams
            
    def isAnagramOfGroups(self, groups, str1):
        for i, item in enumerate(groups):
            if self.isAnagram(item[0], str1):
                return (i, True)
        return (-1, False)

    def isAnagram(self, str1, str2):
        if len(str1) != len(str2): return False

        charS = set(str1)

        for c in charS:
            if str1.count(c) != str2.count(c):
                return False
                
        return True
    
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