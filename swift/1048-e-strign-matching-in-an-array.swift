// https://leetcode.com/problems/string-matching-in-an-array/
class Solution {
    func stringMatching(_ words: [String]) -> [String] {

        var result: [String] = []

        for (i, val) in words.enumerated() {
            let others = Array(words[..<i]) + Array(words[(i+1)..<words.count])
            for o in others {
                if o.contains(val) {
                    result.append(val)
                    break
                }
            }
        }

        return result
    }
}