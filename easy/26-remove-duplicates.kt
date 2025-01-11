class Solution {
    fun removeDuplicates(nums: IntArray): Int {
    
        var prev = nums.first()
        var prevIndex = 1
        nums.forEachIndexed { i, num ->

            if (i > 0 && prev != num) {
                nums[prevIndex] = num
                prev = num
                prevIndex += 1
            }
        }

        return prevIndex
    }
}