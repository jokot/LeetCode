// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
class Solution {
    func check(_ nums: [Int]) -> Bool {
        var index = 0
        var current = 0

        for (i, n) in nums.enumerated() {
            if current > n {
                index = i
                break
            }
            current = n
        }

        current = 0
        for n in Array(nums[index...]+nums[..<index]) {
            if current > n {
                return false
            }
            current = n
        }

        return true
    }
}