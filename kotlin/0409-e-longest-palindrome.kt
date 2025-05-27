// https://leetcode.com/problems/longest-palindrome/
class Solution {
    fun longestPalindrome(s: String): Int {
        val seen = mutableSetOf<Char>()
        var result = 0

        for (char in s) {
            if (char in seen) {
                result += 2
                seen.remove(char)
            } else {
                seen.add(char)
            }
        }

        if (seen.isNotEmpty()){
            result += 1
        }

        return result
    }
}