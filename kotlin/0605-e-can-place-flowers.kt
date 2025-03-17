// https://leetcode.com/problems/can-place-flowers/
class Solution {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        if (n == 0) return true

        var count = n
        for (i in 0 until flowerbed.size) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.size-1 || flowerbed[i+1] == 0)) {
                flowerbed[i] = 1
                count--
                if (count == 0) return true
            }
        }

        return false
    }
}