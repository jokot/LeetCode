// https://leetcode.com/problems/maximum-score-after-splitting-a-string
class Solution {
    fun maxScore(s: String): Int {
        var left = 0
        var right = s.count { it == '1' }
        var max = 0

        for (i in 0 until s.lastIndex) {
            if (s[i] == '0') {
                left++
            } else {
                right--
            }
            max = maxOf (max, left+right)
        }

        return max
    }
}