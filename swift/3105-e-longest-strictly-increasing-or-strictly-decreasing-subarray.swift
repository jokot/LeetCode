// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
class Solution {
    func longestMonotonicSubarray(_ nums: [Int]) -> Int {
        var result = 1
        var inc = 1
        var dec = 1

        for i in 0..<nums.count-1 {
            let delta = nums[i] - nums[i+1]
            if delta > 0 {
                dec += 1
                inc = 1
            } else if delta < 0 {
                dec = 1
                inc += 1
            } else {
                dec = 1
                inc = 1
            }

            result = max(result, dec, inc)
        }

        return result
    }
}