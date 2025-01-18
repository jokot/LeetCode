class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sMap = {}
        tMap = {}

        for i, c in enumerate(s):
            sMap[c] = sMap.get(c, 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        for key, val in sMap.items():
            if tMap.get(key, 0) != val: return False

        return True

if __name__ == '__main__':
    print(Solution().isAnagram("anagram","gramana"))
    print(Solution().isAnagram("car","rat"))
    print(Solution().isAnagram("c","car"))