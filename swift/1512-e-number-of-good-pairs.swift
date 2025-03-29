// https://leetcode.com/problems/number-of-good-pairs/
class Solution {
    func numIdenticalPairs(_ nums: [Int]) -> Int {
        var counts : [Int: Int] = [:]

        for num in nums {
            counts[num, default:0] += 1
        }

        var result = 0
        for c in counts.values {
            result += (c * (c - 1)) / 2
        }

        return result
    }
}