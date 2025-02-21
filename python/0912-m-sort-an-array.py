from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums

    def mergeSort(self, nums):
        if len(nums) == 1:
            return
            
        left = nums[0:len(nums)//2]
        right = nums[len(nums)//2:]

        self.mergeSort(left)
        self.mergeSort(right)

        pointer_main = 0
        pointer_l = 0
        pointer_r = 0
        
        while pointer_main < len(nums):
            while pointer_l < len(left) or pointer_r < len(right):
                if pointer_l < len(left) and pointer_r < len(right):
                    if left[pointer_l] < right[pointer_r]:
                        nums[pointer_main] = left[pointer_l]
                        pointer_l += 1
                    else:
                        nums[pointer_main] = right[pointer_r]
                        pointer_r += 1
                elif pointer_l < len(left):
                    nums[pointer_main] = left[pointer_l]
                    pointer_l += 1
                else:
                    nums[pointer_main] = right[pointer_r]
                    pointer_r += 1
                pointer_main += 1

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

