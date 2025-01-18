## https://leetcode.com/problems/remove-element
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_no_val = []
        for n in nums:
            if n != val:
                nums_no_val.append(n)

        for i, n in enumerate(nums_no_val):
            nums[i] = n

        return len(nums_no_val)

if __name__ == '__main__':
    print(Solution().removeElement([0,1,1,2,2,3,4,5,1,2,7,5], 2))
    print(Solution().removeElement([0,1,3,4,5,1,2,7,5], 1))
    print(Solution().removeElement([0,1,1,1,1,1,1,1,1], 1))