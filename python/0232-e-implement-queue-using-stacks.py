class MyQueue:

    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        return self.stack1.pop(0)
        

    def peek(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        

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