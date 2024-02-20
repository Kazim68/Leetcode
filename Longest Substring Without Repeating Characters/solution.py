class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx = {}
        l, n = 0, len(s)
        res = 0
        for r in range(n):
            if s[r] not in idx or idx[s[r]] < l:
                res = max(res, r-l+1)
                idx[s[r]] = r
            else:
                l = idx[s[r]]+1
                idx[s[r]] = r
        return res 