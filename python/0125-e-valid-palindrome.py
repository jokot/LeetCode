## https://leetcode.com/problems/valid-palindrome
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans("","", string.punctuation)
        s = s.translate(translator)
        s = s.lower()
        s = s.replace(" ", "")

        return s == s[::-1]

if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome(" "))
    print(Solution().isPalindrome("0P"))