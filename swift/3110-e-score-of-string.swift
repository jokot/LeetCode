// # https://leetcode.com/problems/score-of-a-string/
class Solution {
    func scoreOfString(_ s: String) -> Int {
        var res = 0
        let chars = Array(s)

        for i in 0..<(chars.count - 1) {
            if let ascii1 = chars[i].asciiValue, let ascii2 = chars[i+1].asciiValue {
                res += abs(Int(ascii1) - Int(ascii2))
            }
        }

        return res
    }
}