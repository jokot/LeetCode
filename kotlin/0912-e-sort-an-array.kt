// https://leetcode.com/problems/sort-an-array/

class Solution {
    fun sortArray(nums: IntArray): IntArray {
        mergeSort(nums)
        return nums
    }

    fun mergeSort(nums: IntArray): IntArray {
        if (nums.size == 1) return nums
        
        val left = nums.copyOfRange(0, nums.size/2)
        val right = nums.copyOfRange(nums.size/2, nums.size)

        mergeSort(left)
        mergeSort(right)

        var mainPointer = 0
        var lPointer = 0
        var rPointer = 0

        while (mainPointer < nums.size) {
            while (lPointer < left.size || rPointer < right.size) {
                when {
                    (lPointer < left.size && 
                        rPointer < right.size && 
                        left[lPointer] < right[rPointer]) || rPointer >= right.size -> {
                            nums[mainPointer] = left[lPointer]
                            lPointer++
                        }
                    else -> {
                            nums[mainPointer] = right[rPointer]
                            rPointer++
                        }
                }
                mainPointer++
            }
        }

        return nums
    }
}