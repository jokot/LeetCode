class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {
        
        val rows = mutableMapOf<Int,MutableSet<Char>>()
        val cols = mutableMapOf<Int,MutableSet<Char>>()
        val boxes = mutableMapOf<String,MutableSet<Char>>()

        for (i in 0 until 9) {
            for (j in 0 until 9) {
                if (board[i][j] == '.') {
                    continue
                }
                val alreadyInRows = rows[i]?.contains(board[i][j]) ?: false
                val alreadyInCols = cols[j]?.contains(board[i][j]) ?: false
                val alreadyInBoxes = boxes["${i/3},${j/3}"]?.contains(board[i][j]) ?: false
                // print("$alreadyInRows $alreadyInCols $alreadyInBoxes")
                
                if ( alreadyInRows || alreadyInCols || alreadyInBoxes) return false
                
                if (i !in rows) {
                    rows[i] = mutableSetOf(board[i][j])
                } else {
                    rows[i]?.add(board[i][j])
                }

                if (j !in cols) {
                    cols[j] = mutableSetOf(board[i][j])
                } else {
                    cols[j]?.add(board[i][j])
                }
                
                if ("${i/3},${j/3}" !in boxes) {
                    boxes["${i/3},${j/3}"] = mutableSetOf(board[i][j])
                } else {
                    boxes["${i/3},${j/3}"]?.add(board[i][j])
                }
            }
        }

        return true
    }
}