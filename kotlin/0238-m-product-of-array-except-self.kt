// https://leetcode.com/problems/product-of-array-except-self/
class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val size = nums.size
        val output = IntArray(size) { 1 }

        for (i in 1 until size) {
            output[i] = output[i-1] * nums[i-1]
        }

        var suffix = 1
        for (i in size - 1 downTo 0) {
            output[i] *= suffix
            suffix *= nums[i]
        }

        return output
    }
}