class Solution {
    fun stringMatching(words: Array<String>): List<String> {
        val pairs = mutableListOf<String>()

        for (i in 0 until words.lastIndex) {
            for (j in i + 1 until words.size) {
                if (words[i].contains(words[j])) {
                    pairs.add(words[j])
                } else if (words[j].contains(words[i])) {
                    pairs.add(words[i])
                }
            }
        }

        return pairs.distinct()
    }
}