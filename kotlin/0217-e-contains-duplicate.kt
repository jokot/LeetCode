// https://leetcode.com/problems/contains-duplicate
class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val seen = HashSet<Int>(nums.size)

        for (num in nums) {
            if (!seen.add(num)) {
                return true
            }
        }

        return false
    }
}