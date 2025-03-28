// https://leetcode.com/problems/word-pattern/
class Solution {
    func wordPattern(_ pattern: String, _ s: String) -> Bool {
        var mapping: [Character: String] = [:]
        let sSplit = Array(s.split(separator: " "))
        
        if pattern.count != sSplit.count || Set(pattern).count != Set(sSplit).count{
            return false
        }

        for (c, word) in zip(pattern, sSplit) {
            let seen = mapping[c, default: "-"]

            if seen == "-" {
                mapping[c] = String(word)
            } else if seen != word {
                return false
            }
        }

        return true
    }
}