## https://leetcode.com/problems/contains-duplicate
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,4]))
    print(Solution().containsDuplicate([1,2,3,4,1]))