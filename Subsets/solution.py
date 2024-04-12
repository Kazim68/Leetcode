class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def bk(sub, start):
            res.append(sub[:])
            for i in range(start, n):
                sub.append(nums[i])
                bk(sub, i+1)
                sub.pop()
        bk([], 0)
        return res