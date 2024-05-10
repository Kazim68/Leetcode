class Solution:
    res = ""
    maxLen = 0
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            # for odd size palindrome
            self.expand(i, i, s)
            # for even size palindrome
            self.expand(i, i+1, s)
        return self.res
    
    def expand(self, l, r, s):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            if self.maxLen < r-l+1:
                self.maxLen = r-l+1
                self.res = s[l: r+1]
            l -= 1
            r += 1