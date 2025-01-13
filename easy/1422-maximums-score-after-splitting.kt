class Solution {
    fun maxScore(s: String): Int {
        var max = 0
        for (i in 1 until s.length) {
            val count = s.substring(0, i).filter{ it == '0'}.length + s.substring(i, s.length).filter{ it == '1'}.length
            println(count)
            if ( count > max) {
                max = count
            }
        }

        return max
    }
}