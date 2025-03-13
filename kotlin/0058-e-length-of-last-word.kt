// https://leetcode.com/problems/length-of-last-word/
class Solution {
    fun lengthOfLastWord(s: String): Int {
        var count = 0
        var isFirstEmpty = true

        for (i in s.length -1 downTo 0) {
            if (s[i] != ' ' && isFirstEmpty) {
                isFirstEmpty = false
            }
            if (!isFirstEmpty) {
                if (s[i] == ' ') return count
                count++
            }
        }

        return count
    }
}