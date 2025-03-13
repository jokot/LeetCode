// https://leetcode.com/problems/is-subsequence/
class Solution {
    fun isSubsequence(s: String, t: String): Boolean {
        if (s.length > t.length || (s.length == t.length && s != t)) {
            return false
        }

        if (s.length == 0 || s == t) {
            return true
        }

        var index = 0
        for (i in 0 until t.length) {
            if (s.length == index) {
                return true
            }
            if (s[index] == t[i]) {
                index++
            }
        }

        return index == s.length
    }
}