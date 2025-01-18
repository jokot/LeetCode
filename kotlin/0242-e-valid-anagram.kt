// https://leetcode.com/problems/valid-anagram
class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) return false
        val charCountArray = IntArray(26) { 0 }

        for (c in s.toCharArray()) {
            charCountArray[c - 'a']++
        }

        for (c in t.toCharArray()) {
            charCountArray[c - 'a']--
        }

        for (value in charCountArray) {
            if (value != 0) return false
        }

        return true
    }
}