# https://leetcode.com/problems/destination-city/
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = []
        end = []

        for path in paths:
            start.append(path[0])
            end.append(path[1])
        
        for e in end:
            if e not in start:
                return e