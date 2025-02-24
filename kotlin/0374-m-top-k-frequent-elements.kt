// https://leetcode.com/problems/top-k-frequent-elements/
class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        return getTopK(bucketsSort(counter(nums), nums.size), k)
    }

    fun counter(nums: IntArray): Map<Int, Int> {
        val count = mutableMapOf<Int, Int>()

        for (n in nums) {
            count[n] = count.getOrDefault(n, 0) + 1
        }

        return count
    }

    fun bucketsSort(couter: Map<Int, Int>, size: Int): List<List<Int>> {
        val buckets = MutableList(size + 1) { mutableListOf<Int>() }

        couter.forEach { n, c ->
            buckets[c].add(n)
        }

        buckets.reverse()

        return buckets
    }

    fun getTopK(buckets: List<List<Int>>, k: Int): IntArray {
        val topK = IntArray(k)
        
        var index = 0
        for (b in buckets) {
            for (n in b) {
                topK[index] = n
                index++
                if (index == k) return topK
            }
        }

        return topK
    }
}