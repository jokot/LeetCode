// https://leetcode.com/problems/find-pivot-index/
class Solution {
    fun pivotIndex(nums: IntArray): Int {
        var total = 0

        for (num in nums) {
            total += num
        }

        var left_sum = 0

        for (i in 0 until nums.size) {
            val num = nums[i]
            if (left_sum == (total - left_sum - num)) {
                return i
            }
            left_sum += num
        }

        return -1

    }
}