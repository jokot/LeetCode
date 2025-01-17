// https://leetcode.com/problems/contains-duplicate
class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        if (nums.size < 2) return false
        val numsMap = hashMapOf<Int, Int>()

        nums.forEach { num ->
            numsMap[num] = numsMap.getOrDefault(num, 0) + 1
        }

        for (value in numsMap.values) {
            if (value > 1) return true
        }

        return false
    }
}