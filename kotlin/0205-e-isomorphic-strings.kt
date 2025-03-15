class Solution {
    fun isIsomorphic(s: String, t: String): Boolean {
        val s_to_t = mutableMapOf<Char, Char>()
        val t_to_s = mutableMapOf<Char, Char>()

        for ((cs, ct) in s zip t) {
            if ((cs in s_to_t && s_to_t[cs] != ct) || (ct in t_to_s && t_to_s[ct] != cs)) return false
            else {
                s_to_t[cs] = ct
                t_to_s[ct] = cs
            }
        }

        return true
    }
}