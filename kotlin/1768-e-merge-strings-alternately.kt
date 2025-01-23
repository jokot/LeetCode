// https://leetcode.com/problems/merge-strings-alternately
class Solution {
    fun mergeAlternately(word1: String, word2: String): String {
        val merged = StringBuilder()
        val max = maxOf(word1.length, word2.length)

        for (i in 0 until max) {
            if (i < word1.length) merged.append(word1[i])
            if (i < word2.length) merged.append(word2[i])
        }

        return merged.toString()
    }
}