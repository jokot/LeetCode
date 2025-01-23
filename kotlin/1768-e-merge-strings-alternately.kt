// https://leetcode.com/problems/merge-strings-alternately
class Solution {
    fun mergeAlternately(word1: String, word2: String): String {
        val len1 = word1.length
        val len2 = word2.length
        val max = if (len1 > len2) len1 else len2

        var merged = ""

        for (i in 0 until max) {
            if (i < len1) {
                merged += word1[i]
            }
            if (i < len2) {
                merged += word2[i]
            }
        }

        return merged
    }
}