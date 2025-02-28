
class NumArray(private val nums: IntArray) {
    
    private val prefix = IntArray(nums.size)
    
    init {
        calculateNumsPrefix()
    }

    fun sumRange(left: Int, right: Int): Int {
        if (left == 0) return prefix[right]
        return prefix[right] - prefix[left-1]
    }

    fun calculateNumsPrefix() {
        for (i in 0 until nums.size) {
            if (i == 0) {
                prefix[0] = nums[0]
            } else {
                prefix[i] = nums[i]+prefix[i-1]
            }
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */