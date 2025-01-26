// https://leetcode.com/problems/contains-duplicate-ii
class Solution {
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        val set = mutableSetOf<Int>()

        for (i in 0 until nums.size) {
            if (nums[i] in set) return true

            set.add(nums[i])

            if (set.size > k) {
                set.remove(nums[i-k])
            }
        }

        return false
    }
}