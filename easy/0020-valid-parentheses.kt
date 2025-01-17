// https://leetcode.com/problems/valid-parentheses
class Solution {
    fun isValid(s: String): Boolean {
        if (s.length < 2) return false
        val openings = CharArray(s.length)
        var i = -1
        for (c in s) {
            if (isOpening(c)) {
                openings[++i] = c
            } else {
                if (i > -1 && isMatch(openings[i], c)) {
                    i--
                } else return false
            }
        }

        return i == -1
    }

    fun isOpening(c: Char): Boolean {
        return c == '{' || c == '(' || c == '['
    }

    fun isMatch(opening: Char, c: Char): Boolean {
        return when (c) {
            '}' -> opening == '{'
            ']' -> opening == '['
            ')' -> opening == '('
            else -> false
        }
    }
}