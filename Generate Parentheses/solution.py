class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bk(comb, open, close):
            if close > open or open > n: return
            if open == n:
                res.append(comb+(')' * (n-close)))
                return
            bk(comb+'(', open+1, close)
            bk(comb+')', open, close+1)
        bk("", 0, 0)
        return res