# https://leetcode.com/problems/range-sum-query-immutable/
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums_prefix = [0] * self.n

        self.nums_prefix[0] = nums[0]
        for i in range(1, self.n):
            self.nums_prefix[i] = self.nums_prefix[i - 1] + nums[i]
    
    def sumRange(self, left: int, right: int) -> int:
        return self.nums_prefix[right] if left == 0 else self.nums_prefix[right] - self.nums_prefix[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

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