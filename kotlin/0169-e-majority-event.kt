// https://leetcode.com/problems/majority-element
class Solution {
    fun majorityElement(nums: IntArray): Int {
        var candidate: Int? = null
        var count = 0

        for (num in nums) {
            if (count == 0) {
                candidate = num
                count = 1
            } else if (candidate == num) {
                count++
            } else {
                count--
            }
        }

        return candidate ?: 0
    }
}