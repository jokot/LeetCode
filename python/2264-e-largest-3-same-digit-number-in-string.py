# https://leetcode.com/problems/largest-3-same-digit-number-in-string
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) == 3:
            if len(set(num)) == 1:
                return num
            else:
                return ""
        
        good_integers = []

        for i in range(len(num)-2):
            sub = num[i:i+3]
            if len(set(sub)) == 1:
                good_integers.append(sub)
        
        if not good_integers:
            return ""

        result = good_integers[0]
        temp = int(good_integers[0])

        for i in good_integers:
            if int(i) > temp:
                temp = int(i)
                result = i
        return result

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         for m in ["999","888", "777", "666", "555", "444","333","222","111","000"]:
#             if m in num:
#                 return m

#         return ""   

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("11122233", "222"),          # Multiple options, returns largest
        ("6777133339", "777"),        # Largest possible 3-digit same number
        ("2300019", "000"),           # Contains zeros
        ("42352338", ""),             # No three consecutive same digits
        ("111", "111"),               # Exactly three same digits
        ("123", ""),                  # Three different digits
        ("999999", "999"),            # Multiple occurrences of same digit
        ("12345", ""),                # No three consecutive same digits
        ("444999444", "999"),         # Multiple groups, returns largest
    ]
    
    # Run tests
    for i, (num, expected) in enumerate(test_cases, 1):
        result = solution.largestGoodInteger(num)
        print(f"Test {i}:")
        print(f"Input: {num}")
        print(f"Expected: '{expected}'")
        print(f"Result: '{result}'")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print()
        