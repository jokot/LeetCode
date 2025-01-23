## https://leetcode.com/problems/merge-sorted-array
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        current = m + n - 1
        while current > -1:
            if left > -1 and right > -1 :
                if nums2[right] > nums1[left]:
                    nums1[current] = nums2[right]
                    right -= 1
                else:
                    nums1[current] = nums1[left]
                    left -= 1
            elif left < 0 :
                nums1[current] = nums2[right]
                right -= 1
            else:
                nums1[current] = nums1[left]
                left -= 1

            current -= 1


if __name__ == '__main__':
    arr1 = [1,2,3,0,0,0]
    arr2 = [2,5,6]
    m = 3
    n = 3

    print(arr1)
    Solution().merge(arr1, m, arr2, n)
    print(arr1)