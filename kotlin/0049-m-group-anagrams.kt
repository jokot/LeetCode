// https://leetcode.com/problems/group-anagrams/

class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val groups = mutableMapOf<List<Int>, MutableList<String>>()

        for (str in strs) {
            val key = createKey(str)

            if (key in groups) {
                groups[key]?.add(str)
            } else {
                groups[key] = mutableListOf(str)
            }
        }

        return groups.values.toList()
    }

    fun createKey(str: String): List<Int> {
        val keys = MutableList(26) { 0 }

        for (c in str) {
            keys[c.toInt() - 'a'.toInt()] += 1
        }

        return keys
    }
}