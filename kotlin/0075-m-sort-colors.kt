// https://leetcode.com/problems/sort-colors/
class Solution {
    fun sortColors(nums: IntArray): Unit {
        var i = 0
        var left = 0
        var right = nums.size-1

        fun swap(l: Int, r: Int) {
            val temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
        }   


        while (i <= right) {
            if (nums[i] == 0) {
                swap(i, left)
                left++
            } else if (nums[i] == 2) {
                swap(i, right)
                right--
                i--
            }
            i++
        }
    }
\}