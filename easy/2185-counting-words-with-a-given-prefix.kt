class Solution {
    fun prefixCount(words: Array<String>, pref: String): Int {
        var count = 0

        words.forEach { word ->
            if (word.startsWith(pref)) count += 1
        }

        return count
    }

}