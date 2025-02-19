// https://leetcode.com/problems/remove-element/
class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var pointer = -1
        var counterVal = 0

        for (i in 0 until nums.size) {
            if (nums[i] == `val`) {
                if (pointer == -1) {
                    pointer = i
                }
                counterVal++
            } else if (pointer > -1) {
                nums[pointer] = nums[i]
                pointer++
            }
        }

        return nums.size - counterVal
    }
}