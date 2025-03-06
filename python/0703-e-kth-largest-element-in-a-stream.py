from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.nums = nums
        
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums)-self.kth]
        

# Test runner
if __name__ == "__main__":
    # Test data
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    print(kthLargest.add(3))  # returns 4
    print(kthLargest.add(5))  # returns 5
    print(kthLargest.add(10)) # returns 5
    print(kthLargest.add(9))  # returns 8
    print(kthLargest.add(4))  # returns 8
