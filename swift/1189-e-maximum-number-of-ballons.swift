// https://leetcode.com/problems/maximum-number-of-balloons/
class Solution {
    func maxNumberOfBalloons(_ text: String) -> Int {
        var one : [Character : Int] = [:]
        var two : [Character : Int] = [:]

        for c in text {
            if c == "b" || c == "a" || c == "n" {
                one[c] = 1 + one[c, default: 0]
            } else if c == "l" || c == "o" {
                two[c] = 1 + two[c, default: 0]
            }
        }

        if one.count != 3 || two.count != 2 {
            return 0
        }

        return min(one.values.min() ?? 0, (two.values.min() ?? 0) / 2)
    }
}