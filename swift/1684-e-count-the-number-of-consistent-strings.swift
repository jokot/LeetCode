// https://leetcode.com/problems/count-the-number-of-consistent-strings/
class Solution {
    func countConsistentStrings(_ allowed: String, _ words: [String]) -> Int {
        var count = 0

        for word in words {
            var isIn = true

            for c in Set(word) {
                if !allowed.contains(c) {
                    isIn = false
                    break
                }
            }
            if isIn {
                count += 1
            }
        }

        return count
    }
}