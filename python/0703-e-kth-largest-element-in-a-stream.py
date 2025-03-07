from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.kth = nums, k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.kth:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
        

# Test runner
if __name__ == "__main__":
    # Test data
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    
    assert kthLargest.add(3) == 4, "Test case 1 failed"
    assert kthLargest.add(5) == 5, "Test case 2 failed"
    assert kthLargest.add(10) == 5, "Test case 3 failed"
    assert kthLargest.add(9) == 8, "Test case 4 failed"
    assert kthLargest.add(4) == 8, "Test case 5 failed"
    
    print("All test cases passed!")
