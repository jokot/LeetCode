// https://leetcode.com/problems/two-sum
class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val seen = HashMap<Int,Int>()

        for (i in 0 until nums.size) {
            val left = target - nums[i]
            if (seen.containsKey(left)) return intArrayOf(seen[left]!!, i)
            seen[nums[i]] = i
        }

        return intArrayOf()
    }
}