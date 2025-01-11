class Solution {
    fun removeDuplicates(nums: IntArray): Int {
    
        var counter = 0
        for (i in 1 until nums.size) {
            if (nums[counter] != nums[i]) {
                counter++
                nums[counter] = nums[i]
            }
        }    

        return counter + 1
    }
}