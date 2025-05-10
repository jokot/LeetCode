// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
class Solution {
    func maxProductDifference(_ nums: [Int]) -> Int {
        var a = 10000
        var b = 10000
        var c = 0
        var d = 0

        for n in nums {
            if n <= a {
                b = a
                a = n
            } else if n <= b {
                b = n
            }

            if n >= d {
                c = d
                d = n
            } else if n >= c {
                c = n
            }
        }

        return c*d - a*b
    }
}