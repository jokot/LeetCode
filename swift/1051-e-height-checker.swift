// https://leetcode.com/problems/height-checker/
class Solution {
    func heightChecker(_ heights: [Int]) -> Int {
        var result = 0
        
        for (m, n) in zip(heights, heights.sorted()) {
            if m != n {
                result += 1
            }
        }

        return result
    }
}