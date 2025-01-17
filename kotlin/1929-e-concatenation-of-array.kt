// https://leetcode.com/problems/concatenation-of-array
class Solution {
    fun getConcatenation(nums: IntArray): IntArray {
        val n = nums.size
        val ans = IntArray(n * 2)

        System.arraycopy(nums, 0, ans, 0, n)
        System.arraycopy(nums, 0, ans, n, n)

        return ans
    }
}