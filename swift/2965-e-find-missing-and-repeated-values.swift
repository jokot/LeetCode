// https://leetcode.com/problems/find-missing-and-repeated-values/
class Solution {
    func findMissingAndRepeatedValues(_ grid: [[Int]]) -> [Int] {
        let n = grid.count
        var seen : Set<Int> = []
        var repeated = 0

        for row in grid {
            for cell in row {
                if seen.contains(cell) {
                    repeated = cell
                }
                seen.insert(cell)
            }
        }

        for i in 1...(n*n+1) {
            if !seen.contains(i) {
                return [repeated, i]
            }
        }

        return [0,0]
    }
}