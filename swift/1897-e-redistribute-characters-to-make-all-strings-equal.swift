class Solution {
    func makeEqual(_ words: [String]) -> Bool {
        let n = words.count

        var counter : [String: Int] = [:]
        for word in words{
            for c in word {
                counter[String(c), default: 0] += 1
            }
        }

        for val in counter.values {
            if val % n != 0 {
                return false
            }
        }

        return true
    }
}