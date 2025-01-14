class Solution {
    fun countPrefixSuffixPairs(words: Array<String>): Int {
        var count = 0
        for (i in 0 until words.size - 1) {
            for (j in i+1 until words.size) {
                if (isPrefixAndSuffix(words[i], words[j])) {
                    count++
                }
            }
        }
        return count
    }

    fun isPrefixAndSuffix(str1: String, str2: String): Boolean {
        if (str1.length > str2.length) return false
        return str1 == str2.substring(0, str1.length) && str1 == str2.substring(str2.length - str1.length, str2.length)
    }
}