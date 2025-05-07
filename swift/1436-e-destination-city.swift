
class Solution {
    func destCity(_ paths: [[String]]) -> String {
        var start: [String] = []
        var end: [String] = []

        for path in paths {
            start.append(path[0])
            end.append(path[1])
        }

        for e in end {
            if !start.contains(e) {
                return e
            }
        }

        return ""
    }
}