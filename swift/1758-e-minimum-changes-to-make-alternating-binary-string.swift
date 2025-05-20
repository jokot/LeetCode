// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
class Solution {
    func minOperations(_ s: String) -> Int {
        var countEven = 0
        var countOdd = 0

        for (i, c) in s.enumerated() {
            if i % 2 == 0 {
                if c == "0" {
                    countEven += 1
                } else {
                    countOdd += 1
                }
            } else {
                if c == "1" {
                    countEven += 1
                } else {
                    countOdd += 1
                }
            }
        }

        return min(countEven, countOdd)
    }
}