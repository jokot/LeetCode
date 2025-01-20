// https://leetcode.com/problems/design-hashmap
data class MyListNode(
    val key: Int,
    val value: Int,
    var next: MyListNode?
)

class MyHashMap() {
    private val size = 10007
    private val mult = 1000019
    private val data = arrayOfNulls<MyListNode>(size)

    fun hash(key: Int): Int {
        return ((key.toLong() * mult % size + size) % size).toInt()
    }

    fun put(key: Int, value: Int) {
        remove(key)
        val index = hash(key)
        val node = MyListNode(key, value, data[index])
        data[index] = node
    }

    fun get(key: Int): Int {
        val index = hash(key)
        var node = data[index]
        while (node != null) {
            if (node.key == key) return node.value
            node = node.next
        }

        return -1
    }

    fun remove(key: Int) {
        val index = hash(key)
        var node: MyListNode? = data[index]

        if (node == null) return
        if (node.key == key) {
            data[index] = node.next
            return
        }

        while (node?.next != null) {
            if (node.next!!.key == key) {
                node.next = node.next!!.next
                return
            }
            node = node.next
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */