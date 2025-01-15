class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        var common = ""
        val sortedStrs = strs.sortedBy { it.length }

        if (sortedStrs.size == 1) return strs[0]
        if (sortedStrs[0].length == 0) return common
        
        var checking = true
        var check = sortedStrs[0][0]
        var index = 0

        while (checking) {
            for (str in sortedStrs) {
                if (str.length < index) {
                    checking = false
                    break
                }
                if (check != str[index]) {
                    checking = false
                    break
                }
            }
            if (checking) {
                common += sortedStrs[0][index]
                index ++
                if (sortedStrs[0].length > index) {
                    check = sortedStrs[0][index]
                } else {
                    checking = false
                }
            }
        }

        return common
    }
}