## https://leetcode.com/problems/reverse-string
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) -1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

if __name__ == '__main__':
    arr1 = ["h","e","l","l","o"]
    print(arr1)
    Solution().reverseString(arr1)
    print(arr1)

    arr2 = ["H","a","n","n","a","h"]
    print(arr2)
    Solution().reverseString(arr2)
    print(arr2)

    arr3 = ["p","l","a","n",","," ","a"," ","c","a","n","a"]
    print(arr3)
    Solution().reverseString(arr3)
    print(arr3)
