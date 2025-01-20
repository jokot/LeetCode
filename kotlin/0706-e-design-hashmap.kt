// https://leetcode.com/problems/design-hashmap
class MyHashMap() {
    private val buckets = IntArray(1000001) { -1 }

    fun put(key: Int, value: Int) {
        buckets[key] = value
    }

    fun get(key: Int): Int {
        return buckets[key]
    }

    fun remove(key: Int) {
        buckets[key] = -1
    }

}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */