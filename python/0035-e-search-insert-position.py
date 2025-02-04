# https://leetcode.com/problems/search-insert-position
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # 4
        # 1,2,3,5,6,7,8
        # 0,1,2,3,4,5,6
        # return right + 1

        # 9
        # 1,2,3,4,5,6,7,8,10,11
        # 0,1,2,3,4,5,6,7,8 ,9
        # return left

        # 7
        # 1,2,5,6
        # 0,1,2,3
        # return len(nums)

        # 1
        # 2,3,4,6
        # 0,1,2,3
        # return 0

        left = 0
        right = len(nums) - 1
        if nums[left] > target:
            return 0
        if nums[right] < target:
            return len(nums)

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
                if nums[right] < target:
                    return right + 1
            else:
                left = mid
                if nums[left] > target:
                    return left
        
        return left

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (nums, target, expected_output)
    test_cases = [
        ([1,3,5,6], 5, 2),           # Target exists in array
        ([1,3,5,6], 2, 1),           # Target should be inserted in middle
        ([1,3,5,6], 7, 4),           # Target should be inserted at end
        ([1,3,5,6], 0, 0),           # Target should be inserted at beginning
        ([1], 0, 0),                 # Single element array, insert at beginning
        ([1,2,3,5,6,7,8], 4, 3),    # From your example comments
        ([1,2,3,4,5,6,7,8,10,11], 9, 8),  # From your example comments
        ([1,2,5,6], 7, 4),          # From your example comments
        ([2,3,4,6], 1, 0),          # From your example comments
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.searchInsert(nums, target)
        print(f"Test Case {i}:")
        print(f"Array: {nums}")
        print(f"Target: {target}")
        print(f"Expected insert position: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)