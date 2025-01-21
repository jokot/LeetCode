## https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ""
        for c in s:
            if c.isalnum():
                cleanS += c.lower()

        for i in range(len(cleanS)//2):
            if cleanS[i] != cleanS[len(cleanS)-1-i]: return False

        return True

if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome(" "))
    print(Solution().isPalindrome("0P"))