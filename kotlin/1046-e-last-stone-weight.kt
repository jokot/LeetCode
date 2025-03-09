// https://leetcode.com/problems/last-stone-weight/
class Solution {
    fun lastStoneWeight(stones: IntArray): Int {
        
        if (stones.size == 1) return stones[0]

        val maxHeap = PriorityQueue<Int>()
        stones.forEach { maxHeap.add(it * -1) }
        
        while (maxHeap.size > 1) {
            val a = maxHeap.poll()
            val b = maxHeap.poll()
            val result = abs(a-b)
            maxHeap.add(result * -1)
        }

        return maxHeap.peek() * -1
    }
}