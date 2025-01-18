## https://leetcode.com/problems/majority-element
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = {}

        for n in nums:
            nums_map[n] = nums_map.get(n, 0) + 1

        maxCount = max(nums_map.values())

        for key, value in nums_map.items():
            if maxCount == value:
                return key

        return 0

if __name__ == '__main__':
    print(Solution().majorityElement([1,1,1,1,2,2,2,2,3,4,5,6]))
