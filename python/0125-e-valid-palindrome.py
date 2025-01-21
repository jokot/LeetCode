## https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ""
        for c in s:
            lower = ord(c) - ord('a')
            upper = ord(c) - ord('A')
            number = ord(c) - ord('0')

            if lower in range(0, 26) or number in range(0, 10):
                cleanS += c
            elif upper in range(0, 26):
                cleanS += chr(ord('a') + upper)

        for i in range(len(cleanS)//2):
            if cleanS[i] != cleanS[len(cleanS)-1-i]: return False

        return True

if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome(" "))
    print(Solution().isPalindrome("0P"))