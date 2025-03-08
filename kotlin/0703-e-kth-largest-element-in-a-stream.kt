
class KthLargest(private val k: Int, private val nums: IntArray) {

    val minHeap = PriorityQueue<Int>()

    init {
        nums.forEach { minHeap.add(it) }

        while(minHeap.size > k) {
            minHeap.poll()
        }
    }

    fun add(`val`: Int): Int {
        minHeap.add(`val`)
        if (minHeap.size > k) {
            minHeap.poll()
        }
        return minHeap.peek()
    }

}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = KthLargest(k, nums)
 * var param_1 = obj.add(`val`)
 */