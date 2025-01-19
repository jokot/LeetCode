## https://leetcode.com/problems/majority-element
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                count = 1
                candidate = num
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

if __name__ == '__main__':
    print(Solution().majorityElement([1,2,2,1,2,2,2,2,3,4,2,6]))
