# https://leetcode.com/problems/path-crossing/
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        vertical = None
        horizontal = None

        for p in path:
            if vertical != None and horizontal != None:
                if vertical <= 0 or horizontal <= 0:
                    return True
                if p == 'N':
                    vertical += 1
                elif p == 'S':
                    vertical -= 1
                elif p == 'E':
                    horizontal += 1
                else:
                    horizontal -= 1
            elif vertical != None:
                if p == 'N':
                    vertical += 1
                elif p == 'S':
                    vertical -= 1
                elif p == 'E':
                    horizontal = 1
                else:
                    horizontal = 1
            elif horizontal != None:
                if p == 'N':
                    vertical = 1
                elif p == 'S':
                    vertical = 1
                elif p == 'E':
                    horizontal += 1
                else:
                    horizontal -= 1
        
        return False
        