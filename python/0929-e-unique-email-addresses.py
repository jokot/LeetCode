from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def cleanFormat(email):
            parts = email.split('@')
            local = parts[0]
            cleanLocal = ""
            for c in local:
                if c == '+':
                    break
                if c != ".":
                    cleanLocal += c
            domain = parts[1]

            return cleanLocal + "@" + domain
        
        for i in range(len(emails)):
            emails[i] = cleanFormat(emails[i])

        return len(set(emails))

# Test runner
if __name__ == "__main__":
    solution = Solution()
    
    # Test data
    test_cases = [
        (["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"], 2),
        (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"], 3),
        (["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"], 2),
        (["test.email+alex@leetcode.com", "test.email@leetcode.com"], 1),
        (["test.email@leetcode.com"], 1)
    ]
    
    for i, (emails, expected) in enumerate(test_cases):
        assert solution.numUniqueEmails(emails) == expected, f"Test case {i + 1} failed"
    
    print("All test cases passed!")
