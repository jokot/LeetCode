// https://leetcode.com/problems/baseball-game/

class Solution {
    fun calPoints(operations: Array<String>): Int {
        val points = mutableListOf<Int>()

        for (op in operations) {
            when (op) {
                "C" -> {
                    points.removeAt(points.size-1)
                }
                "D" -> {
                    points.add(points[points.size-1] * 2)
                }
                "+" -> {
                    points.add(points[points.size-1] + points[points.size-2])
                }
                else -> {
                    points.add(op.toInt())
                }
            }
        }

        return points.sum()
    }
}