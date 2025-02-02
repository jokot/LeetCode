# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def pop(self) -> int:
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[-1]
        

    def empty(self) -> bool:
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Runner code with sample input
if __name__ == "__main__":
    # Test case 1: Basic operations
    print("Test Case 1: Basic Operations")
    queue = MyQueue()
    operations = [
        ("push", 1),
        ("push", 2),
        ("peek", None),
        ("pop", None),
        ("empty", None)
    ]
    
    for op, val in operations:
        if op == "push":
            print(f"Push {val}")
            queue.push(val)
        elif op == "pop":
            result = queue.pop()
            print(f"Pop -> {result}")
        elif op == "peek":
            result = queue.peek()
            print(f"Peek -> {result}")
        elif op == "empty":
            result = queue.empty()
            print(f"Is Empty? -> {result}")
    print("-" * 50)

    # Test case 2: Empty queue operations
    print("Test Case 2: Empty Queue")
    queue = MyQueue()
    print(f"Is Empty? -> {queue.empty()}")
    print("-" * 50)

    # Test case 3: Multiple operations
    print("Test Case 3: Multiple Operations")
    queue = MyQueue()
    test_values = [1, 2, 3, 4, 5]
    
    print("Pushing values:", test_values)
    for val in test_values:
        queue.push(val)
    
    print("Peek value:", queue.peek())
    
    print("Popping all values:", end=" ")
    while not queue.empty():
        print(queue.pop(), end=" ")
    print("\nIs Empty?", queue.empty())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()