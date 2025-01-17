// https://leetcode.com/problems/contains-duplicate
class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        if (nums.size < 2) return false
        return nums.distinct().size != nums.size
    }
}