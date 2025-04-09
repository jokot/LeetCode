// https://leetcode.com/problems/kth-distinct-string-in-an-array
class Solution {
    func kthDistinct(_ arr: [String], _ k: Int) -> String {
        var count: [String:Int] = [:]
        
        for a in arr {
            count[a, default: 0] += 1
        }

        var kth = k

        for key in arr {
            let val = count[key, default: 0]
            if val == 1 {
                kth -= 1
                if kth == 0 {
                    return key
                }
            }
        }

        return ""
    }
}