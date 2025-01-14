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
        var end = words.length - search.length

        var count = 0

        for (i in 0 .. end) {
            if (
                words[i] == search[0] 
                && words[i+search.lastIndex] == search[search.lastIndex]
            ) {
                for (j in 1 until search.lastIndex) {
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