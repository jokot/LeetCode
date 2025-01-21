// https://leetcode.com/problems/reverse-string
class Solution {
    fun reverseString(s: CharArray): Unit {
        val len = s.size
        for (i in 0 until len/2) {
            val temp = s[i]
            s[i] = s[len-i-1]
            s[len-i-1] = temp
        }
    }
}