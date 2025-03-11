
class Solution {
    fun replaceElements(arr: IntArray): IntArray {
        if (arr.size == 1) return IntArray(1) { -1 }

        var maxx = -1
        for (i in arr.size - 1 downTo 0) {
            val temp = arr[i]
            arr[i] = maxx
            maxx = max(maxx, temp)
        }

        return arr
    }
}