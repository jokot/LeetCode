## https://leetcode.com/problems/merge-strings-alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        merged = ""

        for i in range (0, max(len1, len2)):
            if i < len1:
                merged += word1[i]
            if i < len2:
                merged += word2[i]

        return merged

if __name__ == '__main__':
    print(Solution().mergeAlternately("abc", "pqr"))
    print(Solution().mergeAlternately("ab", "pqrs"))
    print(Solution().mergeAlternately("abcd", "pq"))
