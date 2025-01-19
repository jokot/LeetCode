## https://leetcode.com/problems/design-hashset
class MyHashSet:

    def __init__(self):
        self.values = []

    def add(self, key: int) -> None:
        if key not in self.values:
            self.values.append(key)

    def remove(self, key: int) -> None:
        if key in self.values:
            self.values.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.values

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    print(obj.values)
    obj.add(2)
    print(obj.values)
    obj.remove(1)
    print(obj.values)
    obj.add(3)
    print(obj.values)
    print(obj.contains(3))