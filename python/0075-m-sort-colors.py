from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0

        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
            else:
                blue += 1

        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < red + white:
                nums[i] = 1
            else:
                nums[i] = 2

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

