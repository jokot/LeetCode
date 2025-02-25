// https://leetcode.com/problems/valid-sudoku/
class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {
        val rows = IntArray(9)
        val cols = IntArray(9)
        val boxes = IntArray(9)

        for(i in 0 until 9) {
            for (j in 0 until 9) {
                val v: Int = board[i][j] - '1'
                if (v < 0) continue

                val bits = 1 shl v
                if (rows[i] and bits > 0 || cols[j] and bits > 0) return false

                val r = 3*(i/3) + j/3
                if (boxes[r] and bits > 0) return false

                rows[i] = bits or rows[i]
                cols[j] = bits or cols[j]
                boxes[r] = bits or boxes[r]
            }
        }
        return true
    }
}