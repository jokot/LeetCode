// https://leetcode.com/problems/valid-palindrome-ii
class Solution {
    fun validPalindrome(s: String): Boolean {
        var l = 0
        var r = s.length - 1

        while (l < r) {
            if (s[l] == s[r]) {
                l++
                r--
            } else return validPalindrome(s, l+1, r) || validPalindrome(s, l, r-1)
        }

        return true
    }

    fun validPalindrome(s: String, l: Int, r: Int): Boolean {
        var l = l
        var r = r

        while (l < r) {
            if (s[l] == s[r]) {
                l++
                r--
            } else return false
        }

        return true
    }
}