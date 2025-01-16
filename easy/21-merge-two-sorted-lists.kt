/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        if (list1 == null) return list2
        if (list2 == null) return list1

        var mergedNode = list2
        var current = list1
        while (current != null) {
            mergedNode = insertNode(mergedNode, current?.`val` ?: 0)
            // print("${current.`val`}: ")
            // printListNode(mergedNode)
            current = current?.next
        }

        return mergedNode
    }

    fun printListNode(head: ListNode?) {
        var current = head
        while (current != null) {
            print("${current?.`val`} -> ")
            current = current?.next
        }
        println("null")
    }

    fun insertNode(head: ListNode?, newVal: Int): ListNode? {
        when {
            head == null -> return ListNode(newVal)
            (head?.`val` ?: 0) >= newVal -> {
                val newNode = ListNode(newVal)
                newNode.next = head
                return newNode
            }
            else -> {
                head?.next = insertNode(head?.next, newVal)
                return head
            }
        }
    }
}