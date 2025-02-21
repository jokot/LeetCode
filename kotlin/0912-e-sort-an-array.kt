// https://leetcode.com/problems/sort-an-array/

class Solution {
    fun sortArray(nums: IntArray): IntArray {
        mergeSort(nums, 0, nums.size-1)
        return nums
    }

    fun mergeArray(nums: IntArray, L: Int, M: Int, R: Int): IntArray {
        val left = nums.copyOfRange(L, M+1)
        val right = nums.copyOfRange(M+1, R+1)

        var i = L
        var j = 0
        var k = 0

        while (j < left.size || k < right.size) {
            if ((j < left.size && k < right.size && left[j] < right[k]) || k >= right.size) {
                nums[i] = left[j]
                j++
            } else {
                nums[i] = right[k]
                k++
            }
            i++
        }

        return nums
    }

    fun mergeSort(nums: IntArray, l: Int, r: Int): IntArray {
        if (l == r) return nums
        val m = (l + r)/2
        mergeSort(nums, l, m)
        mergeSort(nums, m+1, r)
        mergeArray(nums, l, m, r)
        return nums
    }
}