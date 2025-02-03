// https://leetcode.com/problems/binary-search/
class Solution {
    fun search(nums: IntArray, target: Int): Int {
        return binarySearch(nums, target, 0, nums.size/2, nums.size-1)
    }

    fun binarySearch(nums: IntArray, target: Int, left: Int, center: Int, right: Int): Int {
        if (left > right) return -1

        if (nums[center] == target) {
            return center
        } else if (nums[center] > target) {
            val r = center - 1
            val c = (left + r) / 2
            return binarySearch(nums, target, left, c, r)
        } else {
            val l = center + 1
            val c = (l + right) / 2
            return binarySearch(nums, target, l, c, right)
        }
    }
}