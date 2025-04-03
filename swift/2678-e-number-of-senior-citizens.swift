// https://leetcode.com/problems/number-of-senior-citizens/
class Solution {
    func countSeniors(_ details: [String]) -> Int {
        var count = 0

        for s in details {
            if let tens = s[s.index(s.startIndex, offsetBy: 11)].wholeNumberValue,
            let ones = s[s.index(s.startIndex, offsetBy: 12)].wholeNumberValue {
                if Int(tens * 10 + ones) > 60 {
                    count += 1
                }
            }
        }
        
        return count
    }
}