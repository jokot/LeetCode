// https://leetcode.com/problems/maximum-ascending-subarray-sum/
class Solution {
    func maxAscendingSum(_ nums: [Int]) -> Int {
        var result = nums[0]
        var inc = nums[0]

        for i in 1..<nums.count{
            if nums[i]-nums[i-1] > 0 {
                inc += nums[i]
            } else {
                inc = nums[i]
            }
            result = max(result, inc)
        }

        return result
    }
}