// https://leetcode.com/problems/design-hashset
class MyHashSet() {
    private val buckets = BooleanArray(1000001)

    fun add(key: Int) {
        buckets[key] = true
    }

    fun remove(key: Int) {
        buckets[key] = false
    }

    fun contains(key: Int): Boolean {
        return buckets[key]
    }

}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */