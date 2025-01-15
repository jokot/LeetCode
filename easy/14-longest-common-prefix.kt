class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        var common = strs[0]
        var length = strs[0].length

        for (i in 1..<strs.size) {
            while (common.length > strs[i].length || common != strs[i].substring(0, length)) {
                length--
                if (length == 0) return ""
                common = common.substring(0, length)
            }
        }

        return common
    }
}