class Solution {
    fun isPalindrome(x: Int): Boolean {
        if (x < 0) {
            return false
        } else if (x < 10) {
            return true
        }

        var reverted = 0
        var original = x

        while (original != 0) {
            reverted *= 10
            reverted += original % 10
            original /= 10
        }

        return reverted == x
    }
}