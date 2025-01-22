// https://leetcode.com/problems/valid-palindrome-ii
class Solution {
    fun validPalindrome(s: String): Boolean {
        return isPalindrome(s, 0, s.length - 1, 1)
    }

    fun isPalindrome(s: String, left: Int, right: Int, bads: Int): Boolean {
        if (bads < 0) return false

        return if (left < right) {
            if (s[left] == s[right]) {
                isPalindrome(s, left+1, right-1, bads)
            } else {
                isPalindrome(s, left+1, right, bads - 1) || isPalindrome(s, left, right-1, bads - 1)
            }
        } else true
    }
}