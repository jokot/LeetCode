
class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size - 1

        while (left <= right) {
            if (nums[left] > target) return left
            else if (nums[right] < target) return right + 1

            val mid = left + (right - left + 1) / 2
            if (nums[mid] == target) {
                return mid
            } else if (nums[mid] > target) {
                right = mid - 1
            } else {
                left = mid
            }
        }

        return 0
    }
}