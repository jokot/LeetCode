// https://leetcode.com/problems/count-the-number-of-consistent-strings/
class Solution {
    func countConsistentStrings(_ allowed: String, _ words: [String]) -> Int {
        var count = 0

        for word in words {
            if Set(word).isSubset(of: Set(allowed)) {
                count += 1
            }
        }

        return count
    }
}