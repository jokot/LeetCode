from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            left = target - n
            if left in seen:
                return [seen[left], i]
            seen[n] = i

        return []

if __name__ == '__main__':
    print(Solution().twoSum([1,2,3], 5))
        