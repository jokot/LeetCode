class Solution {
    fun mySqrt(x: Int): Int {
        if (x == 0) return 0

        var left = 1
        var right = x

        while (left <= right) {
            val mid = left + (right - left) / 2
            val divide = (x/mid).toInt()
            if (divide == mid) return mid
            else if (divide < mid) right = mid - 1
            else left = mid + 1
        }

        return left - 1
    }
}