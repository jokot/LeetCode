// https://leetcode.com/problems/valid-palindrome-ii
class Solution {
    fun validPalindrome(s: String): Boolean {
        return isPalindrome(s, 0, s.length - 1, false)
    }

    fun isPalindrome(s: String, left: Int, right: Int, skip: Boolean): Boolean {
        var l = left
        var r = right

        while (l < r) {
            if (s[l] == s[r]) {
                l++
                r--
            } else if (skip) {
                return false
            } else {
                return isPalindrome(s, l+1, r, true) || isPalindrome(s, l, r-1, true)
            }
        }

        return true
    }
}