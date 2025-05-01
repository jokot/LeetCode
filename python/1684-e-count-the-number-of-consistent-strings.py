# https://leetcode.com/problems/count-the-number-of-consistent-strings/
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        allowedSet = set(allowed)

        for word in words:
            isIn = True
            for c in set(word):
                if c not in allowedSet:
                    isIn = False
                    break
            if isIn:
                count += 1
        
        return count
        