# https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        counter = 0
        for i in range(1, len(nums)):
            if nums[counter] != nums[i]:
                counter += 1
                nums[counter] = nums[i]
        return counter + 1

# Runner code with sample input
if __name__ == "__main__":
    # Sample inputs
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1],
        []
    ]
    
    solution = Solution()
    
    # Test each case
    for nums in test_cases:
        original_nums = nums.copy()  # Keep original for printing
        k = solution.removeDuplicates(nums)
        print(f"Input array: {original_nums}")
        print(f"Number of unique elements: {k}")
        print(f"First {k} elements of modified array: {nums[:k]}")
        print("-" * 50)