// https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue() {
    val s1 = mutableListOf<Int>()
    val s2 = mutableListOf<Int>()

    fun push(x: Int) {
        while(s1.size > 0) {
            s2.add(s1.removeLast())
        }
        s1.add(x)
        while(s2.size > 0) {
            s1.add(s2.removeLast())
        }
    }

    fun pop(): Int {
        return s1.removeLast()
    }

    fun peek(): Int {
        return s1[s1.size-1]
    }

    fun empty(): Boolean {
        return s1.isEmpty()
    }

}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */