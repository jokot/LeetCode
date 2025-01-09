class Solution {
    fun romanToInt(s: String): Int {
        val romanDic = hashMapOf('I' to 1, 'V' to 5, 'X' to 10, 'L' to 50, 'C' to 100, 'D' to 500, 'M' to 1000)
        
        val converted = mutableListOf<Int>()
        
        s.forEachIndexed { i, roman ->
            converted.add(romanDic.getOrDefault(roman, 0))
            if (i > 0 && converted[i-1] < converted[i]) {
                converted[i-1] = converted[i-1] * -1
            }
        }
        
        return converted.sum()
    }
}