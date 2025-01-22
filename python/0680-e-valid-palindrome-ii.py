## https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.validChildPalindrome(s, l+1, r) or self.validChildPalindrome(s, l, r-1)

        return True

    def validChildPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True

if __name__ == '__main__':
    print(Solution().validPalindrome("aba"))
    print(Solution().validPalindrome("aba"))
    print(Solution().validPalindrome("abc"))
    print(Solution().validPalindrome("abbac"))
    print(Solution().validPalindrome("aaaaaaaa"))
    print(Solution().validPalindrome("eeccccbebaeeabebccceea"))
    print(Solution().validPalindrome("eeccccbebaeeabebcccee"))