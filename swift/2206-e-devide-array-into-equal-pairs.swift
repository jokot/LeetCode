class Solution {
    func divideArray(_ nums: [Int]) -> Bool {
        var seen: [Int: Int] = [:]

        for n in nums {
            seen[n] = seen[n, default: 0] + 1
        }

        for (key, val) in seen {
            if val%2 != 0 {
                return false
            }
        }

        return true
    }
}