# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window  = set()

        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])
        
        return False

# Runner code with sample input
if __name__ == "__main__":
    # Sample test cases: (nums, k)
    test_cases = [
        ([1,2,3,1], 3),
        ([1,0,1,1], 1),
        ([1,2,3,1,2,3], 2),
    ]
    
    solution = Solution()
    
    # Test each case
    for nums, k in test_cases:
        result = solution.containsNearbyDuplicate(nums, k)
        print(f"Input array: {nums}")
        print(f"k: {k}")
        print(f"Contains nearby duplicate: {result}")
        print("-" * 50)
        