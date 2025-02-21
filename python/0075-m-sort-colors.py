# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, left, right = 0, 0, len(nums)-1

        def swap(l, r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
        
        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1
            i += 1

# Runner and test cases
def test_sort_colors():
    solution = Solution()

    # Test case 1
    nums = [2, 0, 2, 1, 1, 0]
    expected = [0, 0, 1, 1, 2, 2]
    solution.sortColors(nums)
    assert nums == expected

    # Test case 2
    nums = [2, 0, 1]
    expected = [0, 1, 2]
    solution.sortColors(nums)
    assert nums == expected

    # Test case 3
    nums = [0]
    expected = [0]
    solution.sortColors(nums)
    assert nums == expected

    # Test case 4
    nums = [1]
    expected = [1]
    solution.sortColors(nums)
    assert nums == expected

    # Test case 5
    nums = [2, 2, 2, 1, 1, 0, 0, 0]
    expected = [0, 0, 0, 1, 1, 2, 2, 2]
    solution.sortColors(nums)
    assert nums == expected

    print("All test cases passed!")

if __name__ == "__main__":
    test_sort_colors()

