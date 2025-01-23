// https://leetcode.com/problems/merge-sorted-array
class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        var left = m - 1
        var right = n - 1
        var current = m + n - 1

        while (current > -1) {
            when {
                right > -1 && left > -1 -> {
                    if (nums2[right] > nums1[left]) {
                        nums1[current] = nums2[right]
                        right--
                    } else {
                        nums1[current] = nums1[left]
                        left--
                    }
                }

                left < 0 -> {
                    nums1[current] = nums2[right]
                    right--
                }

                else -> {
                    nums1[current] = nums1[left]
                    left--
                }
            }
            current--
        }
    }
}