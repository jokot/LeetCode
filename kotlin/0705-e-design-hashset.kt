// https://leetcode.com/problems/design-hashset
class MyHashSet() {
    private val size = 1000
    private val buckets = Array(size) { mutableListOf<Int>() }

    fun hash(key: Int): Int {
        return key % size
    }

    fun add(key: Int) {
        val index = hash(key)
        if (key !in buckets[index]) {
            buckets[index].add(key)
        }
    }

    fun remove(key: Int) {
        val index = hash(key)
        if (key in buckets[index]) {
            buckets[index].remove(key)
        }
    }

    fun contains(key: Int): Boolean {
        return key in buckets[hash(key)]
    }

}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */