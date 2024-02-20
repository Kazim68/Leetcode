class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if len(s1) > len(s2): return False

        l, r = 0, n1
        string = sorted(s1)
        while r <= n2:
            if sorted(s2[l:r]) == string: return True
            l+=1
            r+=1
        return False
