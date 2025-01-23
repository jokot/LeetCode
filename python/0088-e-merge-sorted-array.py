## https://leetcode.com/problems/merge-sorted-array
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def insertLeft():
            nonlocal left, current
            nums1[current] = nums1[left]
            left -= 1

        def insertRight():
            nonlocal right, current
            nums1[current] = nums2[right]
            right -= 1

        left = m - 1
        right = n - 1
        current = m + n - 1
        while current > -1:
            if left > -1 and right > -1 :
                if nums2[right] > nums1[left]:
                    insertRight()
                else:
                    insertLeft()
            elif left < 0 :
                insertRight()
            else:
                insertLeft()

            current -= 1


if __name__ == '__main__':
    arr1 = [1,2,3,0,0,0]
    arr2 = [2,5,6]
    m = 3
    n = 3

    print(arr1)
    Solution().merge(arr1, m, arr2, n)
    print(arr1)