# https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
        left_sum = []
        right_sum = []

        for i in range(len(nums)):
            if i == 0:
                left_sum.append(nums[0])
                right_sum.append(nums[len(nums)-1])
            else:
                left_sum.append(nums[i] + left_sum[-1])
                right_sum.append(nums[i] + right_sum[-1])
        right_sum = right_sum[::-1]

        print(left_sum)
        print(right_sum)

        if not right_sum[1]:
            print("a")
            return 0

        for i in range(1, len(nums)-1):
            print(left_sum[i-1], right_sum[i+1])
            print(left_sum[i+1], right_sum[i-1])
            if left_sum[i+1] == right_sum[i-1]:
                print("b")
                return i

        if not left_sum[len(nums)-2]:
            print("c")
            return len(num)-1

        return -1
