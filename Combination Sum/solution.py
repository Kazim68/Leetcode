class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def bk(comb, i, curSum):
            if curSum == target:
                res.append(comb[:])
                return
            if i == len(candidates): return
            if curSum > target:
                return
            
            curSum += candidates[i]
            comb.append(candidates[i])
            bk(comb, i, curSum)
            curSum -= candidates[i]
            comb.pop()

            bk(comb, i+1, curSum)
        
        bk([], 0, 0)
        return res
