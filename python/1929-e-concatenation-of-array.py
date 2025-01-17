## https://leetcode.com/problems/concatenation-of-array
from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

if __name__ == '__main__':
    print(Solution().getConcatenation([1,2,3]))