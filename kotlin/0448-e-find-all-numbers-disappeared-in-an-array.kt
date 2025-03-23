// find-all-numbers-disappeared-in-an-array
class Solution {
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        val existNums = IntArray(nums.size+1) { 0 }

        for (n in nums) {
            existNums[n] = 1
        }
        
        val result = mutableListOf<Int>()

        for (i in 1..nums.size) {
            if (existNums[i] == 0) {
                result.add(i)
            }
        }

        return result
    }
}