## https://leetcode.com/problems/design-hashmap
class MyHashMap:

    def __init__(self):
        self.max_size = 1000001
        self.buckets = [-1 for _ in range(self.max_size)]

    def put(self, key: int, value: int) -> None:
        self.buckets[key] = value

    def get(self, key: int) -> int:
        return self.buckets[key]

    def remove(self, key: int) -> None:
        self.buckets[key] = -1

    def get_values(self) -> list:
        values = []
        for i, n in enumerate(self.buckets):
            if n != -1:
                values.append([i, n])

        return values

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

if __name__ == '__main__':
    my_map = MyHashMap()
    print(my_map.get_values())
    my_map.put(1,1)
    print(my_map.get_values())
    my_map.put(2,2)
    print(my_map.get_values())
    my_map.remove(1)
    print(my_map.get_values())
    my_map.put(3,1)
    print(my_map.get_values())
    my_map.put(4,2)
    print(my_map.get_values())
    my_map.remove(3)
    print(my_map.get_values())