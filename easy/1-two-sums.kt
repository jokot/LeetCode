class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val pair = IntArray(2)
        var isFound = false
        
        for (i in 0 until nums.lastIndex) {
            for (j in i+1 until nums.size) {
                val sum = nums[i] + nums[j]
                if (sum == target) {
                    pair[0] = i
                    pair[1] = j
                    isFound = true
                    break
                }
            }
            if (isFound) {
                break
            }
        }
        
        return pair
    }
}