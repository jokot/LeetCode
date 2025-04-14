# https://leetcode.com/problems/special-array-i/
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = True
            else:
                nums[i] = False
        
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return False

        return True