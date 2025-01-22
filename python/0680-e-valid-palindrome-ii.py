## https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = len(s)//2 + 1
        reversed_half = s[-mid:][::-1]

        if s[:mid] == reversed_half:
            return True

        for i in range (0, mid):
            if s[i] != reversed_half[i]:
                skip_left = s[i+1:mid] == reversed_half[i:mid-1]
                skip_right = s[i:mid-1] == reversed_half[i+1:]
                return skip_left or skip_right

        return True

if __name__ == '__main__':
    print(Solution().validPalindrome("aba"))
    print(Solution().validPalindrome("abca"))
    print(Solution().validPalindrome("abbac"))
    print(Solution().validPalindrome("lccul"))
    print(Solution().validPalindrome("acxcybycxcxa"))
    print(Solution().validPalindrome("eeccccbebaeeabebccceea"))
    print(Solution().validPalindrome("eeccccbebaeeabebcccee"))