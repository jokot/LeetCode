class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        var common = ""
        if (strs.size == 1) return strs[0]
        if (strs[0].length == 0) return common

        var checking = true
        var check = strs[0][0]
        var index = 0

        while (checking) {
            for (str in strs) {
                if (str.length -1 < index) {
                    checking = false
                    break
                }else if (check != str[index]) {
                    checking = false
                    break
                }
            }
            if (checking) {
                common += strs[0][index]
                index ++
                if (strs[0].length > index) {
                    check = strs[0][index]
                } else {
                    checking = false
                }
            }
        }

        return common
    }
}