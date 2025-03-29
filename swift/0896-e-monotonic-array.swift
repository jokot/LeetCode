// https://leetcode.com/problems/monotonic-array/
class Solution {
    func isMonotonic(_ nums: [Int]) -> Bool {
        if nums.count == 1 {
            return true
        }

        var increased = true
        var current = nums[0]

        for i in 1..<nums.count {
            if nums[i] < current {
                increased = false
                break
            }
            current = nums[i]
        }

        var decreased = true
        current = nums[0]

        for i in 1..<nums.count {
            if nums[i] > current {
                decreased = false
                break
            }
            current = nums[i]
        }

        return increased || decreased
    }
}