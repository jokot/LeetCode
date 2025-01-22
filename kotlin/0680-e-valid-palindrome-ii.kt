// https://leetcode.com/problems/valid-palindrome-ii
class Solution {
    fun validPalindrome(s: String): Boolean {
        return isPalindrome(s, 0, s.length - 1, false)
    }

    fun isPalindrome(s: String, left: Int, right: Int, skip: Boolean): Boolean {
        return if (left < right) {
            if (s[left] == s[right]) {
                isPalindrome(s, left+1, right-1, skip)
            } else if (skip) {
                false
            } else {
                isPalindrome(s, left+1, right, true) || isPalindrome(s, left, right-1, true)
            }
        } else true
    }
}