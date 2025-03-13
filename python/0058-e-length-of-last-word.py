# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        clean = s.strip()
        for i in range(len(clean) - 1, -1, -1):
            if clean[i] == " ":
                return count
            count += 1
        
        return count