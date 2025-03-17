# https://leetcode.com/problems/can-place-flowers/
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        
        return False

def test_can_place_flowers():
    solution = Solution()
    
    # Test cases as (flowerbed, n, expected_result)
    test_cases = [
        # Basic test cases
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([1, 0, 0, 0, 0, 1], 2, False),
        
        # Edge cases
        ([0], 1, True),
        ([1], 1, False),
        ([0], 0, True),
        ([1, 0], 1, False),
        
        # All zeros
        ([0, 0, 0, 0], 2, True),
        ([0, 0, 0, 0], 3, False),
        
        # All ones
        ([1, 1, 1], 1, False),
        
        # Alternating patterns
        ([1, 0, 1, 0, 1], 1, False),
        ([0, 1, 0, 1, 0], 1, False),
        
        # Complex cases
        ([1, 0, 0, 0, 0, 0, 1], 2, True),
        ([0, 0, 1, 0, 0], 2, True),
        ([0, 0, 1, 0, 0, 0, 0], 3, True),
        
        # Zero flowers needed
        ([1, 0, 1], 0, True),
        
        # Long sequences
        ([0, 0, 0, 0, 0, 0, 0, 0], 4, True),
        ([0, 0, 0, 0, 0, 0, 0, 0], 5, False)
    ]
    
    # Run tests
    for i, (flowerbed, n, expected) in enumerate(test_cases, 1):
        # Create a copy of flowerbed since the function modifies it
        flowerbed_copy = flowerbed.copy()
        result = solution.canPlaceFlowers(flowerbed_copy, n)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Input: flowerbed = {flowerbed}, n = {n}")
        print(f"Expected: {expected}, Got: {result}")
        if result != expected:
            print(f"Modified flowerbed: {flowerbed_copy}")
        print("-" * 50)
    
    # Print summary
    total_tests = len(test_cases)
    passed_tests = sum(1 for flowerbed, n, expected in test_cases 
                      if solution.canPlaceFlowers(flowerbed.copy(), n) == expected)
    print(f"Summary: {passed_tests}/{total_tests} tests passed")

if __name__ == "__main__":
    test_can_place_flowers()

