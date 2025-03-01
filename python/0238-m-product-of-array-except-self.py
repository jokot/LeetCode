from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        return [prefix[i] * suffix[i] for i in range(len(nums))]

# Runner and test cases
def test_product_except_self():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    result = solution.productExceptSelf(nums)
    assert result == expected

    # Test case 2
    nums = [0, 1, 2, 3, 4]
    expected = [24, 0, 0, 0, 0]
    result = solution.productExceptSelf(nums)
    assert result == expected

    # Test case 3
    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]
    result = solution.productExceptSelf(nums)
    assert result == expected

    # Test case 4
    nums = [2, 3, 4, 5]
    expected = [60, 40, 30, 24]
    result = solution.productExceptSelf(nums)
    assert result == expected

    # Test case 5
    nums = [1, 2, 3, 4, 5]
    expected = [120, 60, 40, 30, 24]
    result = solution.productExceptSelf(nums)
    assert result == expected

    print("All test cases passed!")

if __name__ == "__main__":
    test_product_except_self()
