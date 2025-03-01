// https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix(private val matrix: Array<IntArray>) {

    private val auxRows = matrix.size + 1
    private val auxCols = matrix[0].size + 1

    private val auxMatrix = Array(auxRows) {
        IntArray(auxCols) { 0 }
    }

    init {
        calculateAuxMatrix()
    }

    private fun calculateAuxMatrix() {
        for (i in 1 until auxRows) {
            for (j in 1 until auxCols) {
                auxMatrix[i][j] = (
                    matrix[i-1][j-1]
                    + auxMatrix[i-1][j]
                    + auxMatrix[i][j-1]
                    - auxMatrix[i-1][j-1]
                )
            }
        }
    }

    fun sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int {
        val r1 = row1 + 1
        val r2 = row2 + 1
        val c1 = col1 + 1
        val c2 = col2 + 1

        return (
            auxMatrix[r2][c2]
            - auxMatrix[r2][c1-1]
            - auxMatrix[r1-1][c2]
            + auxMatrix[r1-1][c1-1]
        )
    }

}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */