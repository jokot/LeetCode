// https://leetcode.com/problems/longest-palindrome/
class Solution {
    func longestPalindrome(_ s: String) -> Int {
        var counter : [String:Int] = [:]

        for c in s {
            counter[String(c), default:0] += 1
        }

        var result = 0
        var isOddExist = false

        for val in counter.values {
            if val == 1 {
                isOddExist = true 
            } else if val % 2 == 0 {
                result += val
            } else {
                result += val - 1
                isOddExist = true
            }
        }

        if isOddExist {
            result += 1
        }

        return result
    }
}