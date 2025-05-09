// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
class Solution {
    func maxProductDifference(_ nums: [Int]) -> Int {
        let sNums = nums.sorted()
        let len = sNums.count
        return sNums[len-2]*sNums[len-1] - sNums[0]*sNums[1]
    }
}