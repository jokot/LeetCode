// https://leetcode.com/problems/pascals-triangle/
class Solution {
    fun generate(numRows: Int): List<List<Int>> {
        if (numRows == 1) return listOf(listOf(1))
        if (numRows == 2) return listOf(listOf(1),listOf(1,1))
        
        val pascal_tri = mutableListOf(listOf(1),listOf(1,1))

        for (i in 2 until numRows) {
            val inner = mutableListOf(1)
            val before = pascal_tri[i-1]

            for (j in 0 until before.size-1) {
                inner.add(before[j] + before[j+1])
            }
            inner.add(1)
            
            pascal_tri.add(inner)
        }

        return pascal_tri
    }
}