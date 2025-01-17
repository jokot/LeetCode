// https://leetcode.com/problems/string-matching-in-an-array
class Solution {
    fun stringMatching(words: Array<String>): List<String> {
        val sb = StringBuilder()
        words.forEach {
            sb.append(it)
            sb.append("_")
        }
        val allWords = sb.toString()

        val subs = mutableListOf<String>()
        for (word in words) {
            if (countWordIn(allWords, word) > 1) {
                subs.add(word)
            }
        }

        return subs
    }

    fun countWordIn(words: String, search: String): Int {
        var start = 0
        var end = search.length - 1

        var count = 0

        for (i in 0 .. words.length - 1 - end) {
            if (
                words[i] == search[0] 
                && words[i+end] == search[end]
            ) {
                for (j in 1 until end) {
                    if (words[j+i] != search[j]) {
                        count --
                        break
                    }
                }
                count++
            }
        }

        return count
    }
}