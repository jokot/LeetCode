# https://leetcode.com/problems/sort-an-array/
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        self.mergeSort(nums, 0, len(nums)-1)

        return nums
    
    def mergeArray(self, arr, L, M, R):
        left, right = arr[L:M+1], arr[M+1:R+1]
        i, j, k = L, 0, 0

        while j < len(left) or k < len(right):
            if (j < len(left) and 
                k < len(right) and 
                left[j] < right[k]) or k >= len(right) :
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        return arr

    def mergeSort(self, nums, l, r):
        if l == r:
            return nums
        
        m = (l + r) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m+1, r)
        self.mergeArray(nums,l,m,r)

        return nums

# Runner and test cases
def test_sort_array():
    solution = Solution()

    # Test case 1
    nums = [5, 2, 3, 1]
    expected = [1, 2, 3, 5]
    result = solution.sortArray(nums)
    assert result == expected

    # Test case 2
    nums = [5, 1, 1, 2, 0, 0]
    expected = [0, 0, 1, 1, 2, 5]
    result = solution.sortArray(nums)
    assert result == expected

    # Test case 3
    nums = [3, 2, 1]
    expected = [1, 2, 3]
    result = solution.sortArray(nums)
    assert result == expected

    # Test case 4
    nums = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    result = solution.sortArray(nums)
    assert result == expected

    # Test case 5
    nums = [2, 3, 1, 5, 4]
    expected = [1, 2, 3, 4, 5]
    result = solution.sortArray(nums)
    assert result == expected

    print("All test cases passed!")

if __name__ == "__main__":
    test_sort_array()

