
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def replace(S, T):
            seenS = set()
            seenT = set()
            newT = T
            for i in range(len(S)):
                c = S[i]
                cT = newT[i]
                if c not in seenS and cT not in seenT :
                    seenS.add(c)
                    seenT.add(cT)

                    part = newT[i:].replace(cT,c)
                    newT = newT[:i]+part
                    
                    print(cT, c, newT)
            
            print(s,t,seenS,newT)
            return newT == S
        
        left = replace(s,t)
        right = replace(t,s)
        print(left, right)
            
        return left and right
    