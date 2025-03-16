class Solution {
    fun isIsomorphic(s: String, t: String): Boolean {
        val sToT = IntArray(256) { -1 }
        val tToS = IntArray(256) { -1 }

        for (i in s.indices) {
            val sCode = s[i].code
            val tCode = t[i].code

            if (sToT[sCode] != tToS[tCode]) return false

            sToT[sCode] = i
            tToS[tCode] = i
        }

        return true
    }
}