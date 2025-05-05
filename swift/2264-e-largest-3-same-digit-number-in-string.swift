// # https://leetcode.com/problems/largest-3-same-digit-number-in-string
class Solution {
    func largestGoodInteger(_ num: String) -> String {
        for n in ["999","888","777","666","555","444","333","222","111","000"] {
            if num.contains(n) {
                return n
            }
        }

        return ""
    }
}