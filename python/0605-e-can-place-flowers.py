from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0
        
        for i in range(len(flowerbed)):
            if i > 0 and i < len(flowerbed) - 1:
                if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                    print(1)
                    flowerbed[i] = 1
                    n -= 1
            elif i == 0 and not flowerbed[0] and not flowerbed[1]:
                print(0)
                flowerbed[i] = 1
                n -= 1
            elif i == len(flowerbed) - 1 and not flowerbed[i] and not flowerbed[i-1]:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

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

