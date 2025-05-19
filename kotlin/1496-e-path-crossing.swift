// https://leetcode.com/problems/path-crossing/
class Solution {
    func isPathCrossing(_ path: String) -> Bool {
        var seen = [(0, 0)]

        for c in path {
            var coor = seen[seen.count-1]
            if c == "N" {
                coor = (coor.0, coor.1 + 1)
            } else if c == "S" {
                coor = (coor.0, coor.1 - 1)
            } else if c == "E" {
                coor = (coor.0 + 1, coor.1)
            } else {
                coor = (coor.0 - 1, coor.1)
            }
            
            if seen.contains(where: { element in
                return element == coor
            }) {
                return true
            }
            seen.append(coor)
        }

        return false
    }
}