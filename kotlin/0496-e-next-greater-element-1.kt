// https://leetcode.com/problems/next-greater-element-i
class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        val stack = mutableListOf<Int>()
        val next_greater = mutableMapOf<Int,Int>()

        for (num in nums2) {
            while (stack.size != 0 && stack[stack.size-1] < num) {
                next_greater[stack.removeLast()] = num
            }
            stack.add(num)
        }

        for (num in stack) {
            next_greater[num] = -1
        }
        
        return IntArray(nums1.size) { i-> next_greater[nums1[i]] ?: 0 }
    }
}