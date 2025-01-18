class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        charSet = set(s)

        for c in charSet:
            if (s.count(c) != t.count(c)):
                return False

        return True
        

if __name__ == '__main__':
    print(Solution().isAnagram("anagram","gramana"))
    print(Solution().isAnagram("car","rat"))
    print(Solution().isAnagram("c","car"))