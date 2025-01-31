# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack() {
    private val data = ArrayDeque<Int>()

    fun push(x: Int) {
        data.addLast(x)
    }

    fun pop(): Int {
        return data.removeLast()
    }

    fun top(): Int {
        return data.last()
    }

    fun empty(): Boolean {
        return data.size == 0
    }

}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */