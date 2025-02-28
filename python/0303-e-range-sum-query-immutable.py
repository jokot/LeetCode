# https://leetcode.com/problems/range-sum-query-immutable/
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_prefix = self.calculate_prefix(nums)
    
    def calculate_prefix(self, nums):
        nums_prefix = []
        for i in range(len(nums)):
            if i == 0:
                nums_prefix.append(nums[0])
            else:
                nums_prefix.append(nums[i] + nums_prefix[len(nums_prefix) - 1])
        return nums_prefix
    
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums_prefix[right]
        return self.nums_prefix[right] - self.nums_prefix[left - 1]

# Runner and test cases
def test_num_array():
    # Test case 1
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    assert num_array.sumRange(0, 2) == 1
    assert num_array.sumRange(2, 5) == -1
    assert num_array.sumRange(0, 5) == -3

    # Test case 2
    nums = [1, 2, 3, 4, 5]
    num_array = NumArray(nums)
    assert num_array.sumRange(0, 1) == 3
    assert num_array.sumRange(1, 3) == 9
    assert num_array.sumRange(0, 4) == 15

    # Test case 3
    nums = [1, -1, 1, -1, 1]
    num_array = NumArray(nums)
    assert num_array.sumRange(0, 4) == 1
    assert num_array.sumRange(1, 3) == -1
    assert num_array.sumRange(2, 4) == 1

    # Test case 4
    nums = [0, 0, 0, 0, 0]
    num_array = NumArray(nums)
    assert num_array.sumRange(0, 4) == 0
    assert num_array.sumRange(1, 3) == 0
    assert num_array.sumRange(2, 2) == 0

    # Test case 5
    nums = [1]
    num_array = NumArray(nums)
    assert num_array.sumRange(0, 0) == 1

    print("All test cases passed!")

if __name__ == "__main__":
    test_num_array()