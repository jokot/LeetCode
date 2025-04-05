// https://leetcode.com/problems/string-matching-in-an-array/
class Solution {
    func stringMatching(_ words: [String]) -> [String] {
        if words.count == 1{
            return []
        }

        var result: [String] = []

        for i in 0..<words.count-1 {
            for k in i+1..<words.count {
                if words[i].contains(words[k]) {
                    result.append(words[k])
                } else if words[k].contains(words[i]) {
                    result.append(words[i])
                }
            }
        }

        return Array(Set(result))
    }
}