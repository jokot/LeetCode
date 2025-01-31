
# https://leetcode.com/problems/implement-stack-using-queues/
from collections import deque

class MyStack:

    def __init__(self):
        self.data = deque()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop()
        
    def top(self) -> int:
        return self.data[-1]
        
    def empty(self) -> bool:
        return len(self.data) == 0

# Runner code with sample input
if __name__ == "__main__":
    # Test case 1: Basic operations
    print("Test Case 1: Basic Operations")
    stack = MyStack()
    operations = [
        ("push", 1),
        ("push", 2),
        ("top", None),
        ("pop", None),
        ("empty", None)
    ]
    
    for op, val in operations:
        if op == "push":
            print(f"Push {val}")
            stack.push(val)
        elif op == "pop":
            result = stack.pop()
            print(f"Pop -> {result}")
        elif op == "top":
            result = stack.top()
            print(f"Top -> {result}")
        elif op == "empty":
            result = stack.empty()
            print(f"Is Empty? -> {result}")
    print("-" * 50)

    # Test case 2: Empty stack operations
    print("Test Case 2: Empty Stack")
    stack = MyStack()
    print(f"Is Empty? -> {stack.empty()}")
    print("-" * 50)

    # Test case 3: Multiple operations
    print("Test Case 3: Multiple Operations")
    stack = MyStack()
    test_values = [1, 2, 3, 4, 5]
    
    print("Pushing values:", test_values)
    for val in test_values:
        stack.push(val)
    
    print("Top value:", stack.top())
    
    print("Popping all values:", end=" ")
    while not stack.empty():
        print(stack.pop(), end=" ")
    print("\nIs Empty?", stack.empty())
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()