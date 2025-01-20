## https://leetcode.com/problems/design-hashmap
class ListNode:
    def __init__(self, key, val, nxt):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap:

    def __init__(self):
        self.size = 1007
        self.mult = 10000019
        self.data = [None] * self.size

    def hash(self, key) -> int:
        return key * self.mult % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        index = self.hash(key)
        node = ListNode(key, value, self.data[index])
        self.data[index] = node

    def get(self, key: int) -> int:
        index = self.hash(key)
        node = self.data[index]

        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        node = self.data[index]

        if not node: return
        if node.key == key:
            self.data[index] = node.next
            return

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

if __name__ == '__main__':
    my_map = MyHashMap()
    my_map.put(1,1)
    my_map.put(2,2)
    print(my_map.get(1))
    print(my_map.get(2))
    my_map.remove(1)
    print(my_map.get(1))
    my_map.put(3,1)
    my_map.put(4,2)
    print(my_map.get(3))
    print(my_map.get(4))
    my_map.remove(3)
    print(my_map.get(3))