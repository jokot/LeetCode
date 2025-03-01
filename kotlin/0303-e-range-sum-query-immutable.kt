// https://leetcode.com/problems/range-sum-query-immutable/description/
class NumArray(private val nums: IntArray) {
    
    private val prefix = IntArray(nums.size)
    
    init {
        prefix[0] = nums[0]
        for (i in 1 until nums.size) {
            prefix[i] = prefix[i-1] + nums[i]
        }
    }

    fun sumRange(left: Int, right: Int): Int {
        return if (left == 0) prefix[right] else prefix[right] - prefix[left-1]
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */