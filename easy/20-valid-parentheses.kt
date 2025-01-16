class Solution {
    fun isValid(s: String): Boolean {
        if (s.length < 2) return false
        val openings = mutableListOf<Char>()
        for (c in s) {
            if (isOpening(c)) {
                openings.add(0, c)
            } else {
                if (openings.size > 0 && isMatch(openings[0], c)) {
                    openings.removeFirst()
                } else return false
            }
        }

        return openings.size == 0
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