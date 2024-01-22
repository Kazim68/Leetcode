class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0]
        n = len(nums)
        for num in nums:
            prefix.append(num + prefix[-1])
        res = []
        for q in queries:
            pivot = bisect.bisect(nums, q)
            res.append(q*pivot - prefix[pivot] + prefix[-1] - prefix[pivot] - q*(n - pivot))
        return res