# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Mock guess API implementation
def guess(num: int) -> int:
    # This will be set by our test runner
    global picked_number
    if num > picked_number:
        return -1
    elif num < picked_number:
        return 1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            pick = left + (right - left + 1) // 2

            if guess(pick) == 0:
                return pick
            elif guess(pick) == -1:
                right = pick - 1 
            else: 
                left = pick

        return left  # Changed from return 1 to return left

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (n, picked_number, expected_output)
    test_cases = [
        (10, 6, 6),      # Number in middle
        (1, 1, 1),       # Minimum number
        (2, 1, 1),       # First number of two
        (2, 2, 2),       # Second number of two
        (100, 99, 99),   # Near maximum
        (1000, 500, 500) # Large range, middle number
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (n, pick, expected) in enumerate(test_cases, 1):
        # Set the picked number for our mock guess function
        global picked_number
        picked_number = pick
        
        result = solution.guessNumber(n)
        print(f"Test Case {i}:")
        print(f"Range: 1 to {n}")
        print(f"Picked number: {pick}")
        print(f"Guessed number: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)
        