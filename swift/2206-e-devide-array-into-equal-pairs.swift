class Solution {
    func divideArray(_ nums: [Int]) -> Bool {
        var seen: [Int: Int] = [:]

        for n in nums {
            seen[n] = seen[n, default: 0] + 1
        }

        var totalPair = nums.count / 2

        var count = 0
        for (key, val) in seen {
            count += val / 2
        }

        return count == totalPair
    }
}