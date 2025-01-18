## https://leetcode.com/problems/longest-common-prefix
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        pref_len = len(prefix)
        for i in range(1, len(strs)):
            pref_len = min(pref_len, len(strs[i]))
            while strs[i][0:pref_len] != prefix[0:pref_len]:
                pref_len -= 1
            prefix = prefix[0:pref_len]
            if pref_len == 0:
                break

        return prefix

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flowing"]))
    print(Solution().longestCommonPrefix(["arch", "ac", "a"]))