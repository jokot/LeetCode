// https://leetcode.com/problems/special-array-i/
class Solution {
    func isArraySpecial(_ nums: [Int]) -> Bool {
        var seen : [Bool] = []

        for n in nums {
            seen.append(n%2 == 0)
        }

        for i in 0..<seen.count-1 {
            if seen[i] == seen[i+1] {
                return false
            }
        }
        return true
    }
}