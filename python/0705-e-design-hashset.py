## https://leetcode.com/problems/design-hashset
class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        return key in self.buckets[index]

    def getValues(self) -> list:
        values = []
        for bucket in self.buckets:
            values.extend(bucket)
        return values

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    print(obj.getValues())
    obj.add(2)
    print(obj.getValues())
    obj.remove(1)
    print(obj.getValues())
    obj.add(3)
    print(obj.getValues())
    print(obj.contains(3))