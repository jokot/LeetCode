// https://leetcode.com/problems/pascals-triangle-ii/
class Solution {
    func getRow(_ rowIndex: Int) -> [Int] {
        var result : [Int] = [1]
        for i in 1..<rowIndex+1 {
            result.append(result[result.count-1] * (rowIndex - i + 1) / i)
        }

        return result
    }
}