## https://leetcode.com/problems/design-hashmap
class MyHashMap:

    def __init__(self):
        self.buckets = [None] * 1000001
    
    def put(self, key: int, value: int) -> None:
        self.buckets[key] = value

    def get(self, key: int) -> int:
        val = self.buckets[key]
        return val if val != None else -1

    def remove(self, key: int) -> None:
        self.buckets[key] = None

    def get_values(self) -> list:
        values = []
        for i, n in enumerate(self.buckets):
            if n != None:
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